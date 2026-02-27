from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import csv
from bs4 import BeautifulSoup

import cred

options = webdriver.ChromeOptions()

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
]

options.add_argument(f'user-agent={random.choice(user_agents)}')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--window-size=1920,1080')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)

driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => false,
        });
    """
})

driver.get("https://www.linkedin.com/login")

try:
    wait = WebDriverWait(driver, 20)
    username = wait.until(EC.presence_of_element_located((By.NAME, "session_key")))
    password = wait.until(EC.presence_of_element_located((By.NAME, "session_password")))
except Exception as e:
    print(f"Login page failed to load: {e}")
    print("Current URL:", driver.current_url)
    driver.quit()
    exit()

username.send_keys(cred.USERNAME)
time.sleep(random.uniform(0.5, 1.5))
password.send_keys(cred.PASSWORD)
time.sleep(random.uniform(0.3, 1.0))
password.send_keys(Keys.RETURN)

time.sleep(random.uniform(8, 12)) 

if "feed" not in driver.current_url and "login" in driver.current_url:
    print("Login failed. Check your credentials.")
    driver.quit()
    exit()

search_url = "https://www.linkedin.com/search/results/all/?keywords=aws%20cloud%20club%20ph&origin=SPELL_CHECK_DID_YOU_MEAN&sid=le0&spellCorrectionEnabled=false"
driver.get(search_url)
time.sleep(random.uniform(6, 10))

import urllib.parse
parsed_url = urllib.parse.urlparse(search_url)
query_params = urllib.parse.parse_qs(parsed_url.query)
hashtag = query_params.get('keywords', ['posts'])[0].replace('%23', '').replace('#', '')
csv_filename = f'linkedin_posts_{hashtag}.csv'

for i in range(4):
    print(f"Scrolling... {i+1}/4")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(random.uniform(3, 6)) 

soup = BeautifulSoup(driver.page_source, 'html.parser')
posts = soup.select('.feed-shared-update-v2')

print(f"\nFound {len(posts)} posts. Starting extraction...\n")

posts_data = []

for post in posts:
    try:
        name_element = post.select_one('.update-components-actor__title [aria-hidden="true"]')
        name = name_element.get_text().strip() if name_element else "N/A"

        date_element = post.select_one('.update-components-actor__sub-description')
        date = date_element.get_text().split('•')[0].strip() if date_element else "N/A"

        profile_link = "N/A"
        profile_link_element = post.select_one('.update-components-actor__name a') or \
                               post.select_one('.update-components-actor__title a') or \
                               post.select_one('a[href*="/in/"]')
        
        if profile_link_element and profile_link_element.has_attr('href'):
            temp_link = profile_link_element['href']
            if '/in/' in temp_link:
                profile_id = temp_link.split('/in/')[1].split('?')[0].rstrip('/')
                profile_link = f"https://www.linkedin.com/in/{profile_id}"
            elif temp_link.startswith('/'):
                profile_link = f"https://www.linkedin.com{temp_link}"
            else:
                profile_link = temp_link

        caption_element = post.select_one('.update-components-update-v2__commentary')
        caption = caption_element.get_text().strip() if caption_element else "N/A"

        posts_data.append({
            'Name': name,
            'Profile Link': profile_link,
            'Date': date,
            'Caption': caption
        })

        print(f"Name: {name}")
        print(f"Profile Link: {profile_link}")
        print(f"Post Date: {date}")
        print("-" * 30)

    except Exception as e:
        print(f"Could not parse a post: {e}")
        continue

if posts_data:
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Name', 'Profile Link', 'Date', 'Caption']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(posts_data)
    print(f"\nData successfully saved to {csv_filename}")
else:
    print("No posts found to save.")

driver.quit()