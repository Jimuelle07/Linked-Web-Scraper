# LinkedIn Web Scraper

A powerful web scraper built with Selenium that automates LinkedIn login and extracts post data from search results. This tool allows you to collect user profiles, post dates, captions, and more from LinkedIn based on keyword searches.

## 📋 Project Overview

This project uses Selenium WebDriver to automate LinkedIn searches and scrape post information. It's designed to bypass LinkedIn's anti-bot detection mechanisms while maintaining ethical scraping practices.

### Key Features

- **Automated LinkedIn Login** - Securely logs into LinkedIn using stored credentials
- **Search Automation** - Performs automated keyword searches on LinkedIn
- **Anti-Bot Detection Bypass** - Uses user-agent rotation and CDP commands to avoid detection
- **Post Data Extraction** - Extracts the following information from posts:
  - Author Name
  - Profile Link
  - Post Date
  - Post Caption
- **CSV Export** - Saves all scraped data to a CSV file for easy analysis
- **Error Handling** - Robust error handling for network issues and missing elements

### Project Structure

```
├── main.py              # Main scraper script
├── cred.py              # Credentials file (credentials stored here - DO NOT COMMIT)
├── cleaner.py           # Data cleaning utility
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+** - Download from [python.org](https://www.python.org/downloads/)
- **Google Chrome** - Download from [google.com/chrome](https://google.com/chrome)
- **ChromeDriver** - Matches your Chrome version (automatically handled by webdriver-manager)
- **pip** - Python package manager (usually comes with Python)

## 📦 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/Jimuelle07/Linked-Web-Scraper.git
cd Linked-Web-Scraper
```

### Step 2: Create a Virtual Environment

Using a virtual environment is recommended to avoid package conflicts.

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

Create a `requirements.txt` file with the following packages:

```bash
pip install selenium beautifulsoup4 webdriver-manager
```

Or if you have a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Credentials

Create a `cred.py` file in the project root directory:

```python
# cred.py
USERNAME = "your_linkedin_email@example.com"
PASSWORD = "your_linkedin_password"
```

**⚠️ IMPORTANT SECURITY NOTE:**
- Never commit `cred.py` to version control
- This file is already included in `.gitignore`
- Use strong passwords and consider using environment variables for sensitive credentials in production

### Step 5: Verify Chrome Installation

Make sure Google Chrome is installed. The scraper uses Chrome's WebDriver for automation.

## 🚀 Usage

### Running the Scraper

```bash
python main.py
```

### What Happens

1. **Browser Opens** - A Chrome browser window launches
2. **LinkedIn Login** - Automatically logs into LinkedIn using your credentials
3. **Search Execution** - Performs a search for "aws cloud club ph" (can be customized)
4. **Page Scrolling** - Scrolls through 4 pages of results to load more posts
5. **Data Extraction** - Parses the page HTML and extracts post information
6. **CSV Export** - Saves data to `linkedin_posts_[keywords].csv`

### Customizing the Search Query

To search for different keywords, modify the `search_url` in `main.py`:

```python
search_url = "https://www.linkedin.com/search/results/all/?keywords=YOUR_KEYWORDS_HERE&origin=SPELL_CHECK_DID_YOU_MEAN&sid=le0&spellCorrectionEnabled=false"
```

Replace `YOUR_KEYWORDS_HERE` with your desired search terms (URL-encoded).

## 📊 Output

The scraper generates a CSV file named `linkedin_posts_[keywords].csv` with the following columns:

| Column | Description |
|--------|-------------|
| Name | Author's full name |
| Profile Link | Direct link to the author's LinkedIn profile |
| Date | Post publication date |
| Caption | Full text of the post |

## 🔧 How It Works

### Anti-Bot Detection Mechanisms

The scraper implements several techniques to avoid LinkedIn's anti-bot detection:

1. **User-Agent Rotation** - Randomly selects user-agent strings from modern browsers
2. **CDP Commands** - Uses Chrome DevTools Protocol to hide automation indicators
3. **JavaScript Injection** - Disables the `navigator.webdriver` property
4. **Random Delays** - Adds random sleep intervals between actions to mimic human behavior
5. **Chrome Options** - Disables automation detection features

### Key Components

**WebDriver Configuration**
```
- Disables automation extensions
- Sets a real window size
- Disables GPU acceleration
- Uses sandbox mode
```

**Wait Mechanisms**
```
- Explicit waits for elements to load (max 20 seconds)
- Random delays between actions (0.5-12 seconds)
```

**Data Extraction**
```
- Uses BeautifulSoup to parse HTML
- Selects specific CSS classes for post elements
- Handles missing elements gracefully
```

## 🐛 Troubleshooting

### Login Fails

**Problem**: Script exits with "Login failed. Check your credentials."

**Solutions**:
- Verify your username and password in `cred.py`
- Check if your account requires two-factor authentication (2FA)
- Ensure your LinkedIn account isn't locked due to suspicious activity
- Try logging in manually first to confirm credentials work

### No Posts Found

**Problem**: CSV file is created but contains no data

**Solutions**:
- Increase scroll delay: Change `time.sleep(random.uniform(3, 6))` to a higher value
- Verify the search URL returns results when accessed manually
- Check if LinkedIn has updated their HTML structure (CSS selectors may need updating)
- Wait longer before scrolling: Increase the initial page load wait time

### ChromeDriver Issues

**Problem**: "ChromeDriver not found" or version mismatch errors

**Solutions**:
- The project uses `webdriver-manager` to handle this automatically
- Ensure `selenium` and `webdriver-manager` are properly installed:
  ```bash
  pip install --upgrade selenium webdriver-manager
  ```
- Clear cache and reinstall:
  ```bash
  pip uninstall selenium webdriver-manager
  pip install selenium webdriver-manager
  ```

### Connection Timeouts

**Problem**: Script times out while waiting for elements

**Solutions**:
- Increase wait times in the script:
  ```python
  wait = WebDriverWait(driver, 30)  # Increase from 20 to 30
  ```
- Check your internet connection
- Try adding more random delays between actions

## 🔐 Security Best Practices

1. **Never hardcode credentials** in production - use environment variables:
   ```python
   import os
   USERNAME = os.getenv('LINKEDIN_USERNAME')
   PASSWORD = os.getenv('LINKEDIN_PASSWORD')
   ```

2. **Use `.gitignore`** - Ensure `cred.py` is in your `.gitignore`

3. **LinkedIn Terms of Service** - Always review LinkedIn's ToS as web scraping may violate their policies

4. **Rate Limiting** - The script includes delays to avoid overwhelming LinkedIn's servers

## 🤝 Contributing

To contribute to this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚖️ Legal Notice

This tool is provided for educational and research purposes only. Users are responsible for:
- Complying with LinkedIn's Terms of Service
- Respecting robots.txt and scraping ethics
- Obtaining proper consent when using scraped data
- Not using this tool for malicious or commercial purposes without authorization

## 📞 Support

If you encounter issues:

1. Check the **Troubleshooting** section above
2. Review the error messages and stack traces carefully
3. Check if LinkedIn's website structure has changed
4. Open an issue on GitHub with detailed error information

## 🚀 Future Enhancements

Potential features for future versions:

- Multi-keyword search support
- Database integration for data storage
- Advanced filtering options
- Export to multiple formats (JSON, Excel, etc.)
- Proxy support for higher-volume scraping
- Schedule-based automated scraping
- Dashboard for data visualization
