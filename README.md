# LinkedIn Web Scraper

A web scraper that automates LinkedIn and pulls post data from search results. Basically it logs in, searches for whatever you want, scrolls through the results, and dumps all the post info into a CSV file so you can analyze it later.

## What This Does

The script uses Selenium to drive a Chrome browser, logs into LinkedIn with your credentials, runs a search, and then scrapes all the post info it can find. It's set up to avoid getting blocked by LinkedIn's bot detection by doing things like rotating user agents and adding random delays between actions.

### What You Get

- Your LinkedIn account automatically logs in
- Runs searches for whatever keywords you want
- Grabs author names, their profile links, post dates, and the actual post text
- Saves everything to a CSV file you can open in Excel or wherever
- Handles errors gracefully when stuff doesn't load or is missing

### Project Structure

```
├── main.py              # Main scraper script
├── cred.py              # Credentials file (credentials stored here - DO NOT COMMIT)
├── cleaner.py           # Data cleaning utility
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Getting Started

You'll need Python 3.8 or newer, Google Chrome installed, and pip. That's really it. The script will handle downloading the right ChromeDriver version automatically.

## Installation

**Step 1: Clone it**

```bash
git clone https://github.com/Jimuelle07/Linked-Web-Scraper.git
cd Linked-Web-Scraper
```

**Step 2: Set up a virtual environment** (recommended)

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

**Step 3: Install dependencies**

```bash
pip install selenium beautifulsoup4 webdriver-manager
```

**Step 4: Add your LinkedIn credentials**

Create a file called `cred.py` in the project folder:

```python
USERNAME = "your_email@example.com"
PASSWORD = "your_password"
```

Don't worry, `cred.py` is in the gitignore so it won't get pushed to GitHub. Just keep it safe and use a strong password.

## How to Use It

Just run:

```bash
python main.py
```

A Chrome window will open, log in automatically, search for "aws cloud club ph", scroll through a bunch of results, and save everything to a CSV file. You can change the search terms by editing the `search_url` in `main.py`.

## What You'll Get

The CSV file will have columns for:

- **Name** - Who posted it
- **Profile Link** - Link to their profile
- **Date** - When they posted it
- **Caption** - The actual post text

## How It Avoids Getting Blocked

LinkedIn has bot detection, so the script does a few things to stay under the radar:

- Uses different user-agent strings to look like different browsers
- Injects some JavaScript to hide the `navigator.webdriver` property
- Adds random delays between actions so it doesn't act like a robot
- Disables automation detection features in Chrome

Basically, it tries to act like a human instead of a bot. It's not perfect but it works for reasonable usage.

## Troubleshooting

**Login fails?**

- Double-check your email and password in `cred.py`
- If you have 2FA enabled, you might need to disable it temporarily
- LinkedIn might have locked your account if it detected suspicious activity

**No posts showing up?**

- Try increasing the delay times in the script - maybe LinkedIn's content is loading slower
- Check if LinkedIn changed their HTML (they do that sometimes)
- Make sure the search URL actually returns results when you visit it manually

**ChromeDriver issues?**

- Install/update webdriver-manager: `pip install --upgrade selenium webdriver-manager`
- Make sure you have Chrome installed

**Script timing out?**

- Increase the wait time in the code from 20 seconds to 30 or higher
- Check your internet connection
- Add more delays between actions

## Security Notes

- Don't ever push `cred.py` to GitHub - it's in the gitignore for a reason
- If you're deploying this somewhere, use environment variables instead of hardcoding credentials
- Be aware that web scraping might violate LinkedIn's terms of service - use responsibly
- The script adds delays to be respectful and avoid hammering LinkedIn's servers

## Contributing

Found a bug? Have an idea? Just fork it, make your changes, and open a pull request. That's it.

## License

MIT - do whatever you want with it.

## Legal Stuff

This is for educational and research purposes. If you use it, make sure you're cool with LinkedIn's terms of service. Don't use it to do anything sketchy.
