# WhatsApp Twitter Image Poster Bot

This Python project automates posting the latest tweet images and texts from a specified Twitter account to WhatsApp using Selenium WebDriver for browser automation. It continuously monitors the Twitter account for new tweets with images and sends them to a predefined WhatsApp contact or group via WhatsApp Web.

---

This bot uses Selenium to control a Chrome browser instance with a persistent user profile to stay logged into WhatsApp Web. It scrapes tweet data including timestamps, text content, and images from Twitter’s web interface by executing JavaScript within the browser context. When a new tweet with an image is detected, it downloads the image and uploads it through WhatsApp Web’s UI while sending the tweet text as a message.

The solution solves the problem of sharing Twitter image updates on WhatsApp automatically without relying on official APIs, which often have stricter limitations or require app permissions.

---

### How It Works

- Launches Chrome browser with a user profile that keeps WhatsApp Web logged in.
- Navigates to the specified Twitter user’s page.
- Extracts the latest tweet’s timestamp to detect new tweets.
- Scrapes the tweet text and image URL via JavaScript.
- Downloads the image locally.
- Navigates to WhatsApp Web, opens the specified chat by name, and sends the image with the tweet text as a caption.
- Waits for a fixed interval then repeats the process continuously.

---

### Features

- Fully automated, runs an infinite loop checking every 40 seconds.
- Handles image downloads and file uploads in WhatsApp Web interface.
- Uses Selenium’s explicit waits for reliable UI interaction.
- Can be adapted to post any Twitter user’s latest media to WhatsApp.
- Works without Twitter or WhatsApp APIs by leveraging web scraping and browser automation.

---

### Requirements

- Python 3.7+
- Google Chrome browser installed
- ChromeDriver for your Chrome version correctly installed and in PATH
- Python packages:
  - selenium
  - requests
- Persistent Chrome user data directory (configured in code) to keep WhatsApp Web logged in

---

### Usage

1. Install dependencies:
2. Download ChromeDriver corresponding to your Chrome version and place it in your system PATH.
3. Adjust the `--user-data-dir` path in the code to point to your Chrome user profile folder.
4. Replace the target Twitter username and WhatsApp contact/group name in the code.
5. Run the script:
6. The browser window opens, logs into WhatsApp Web automatically, and the script starts monitoring and posting latest tweets with images.

---

### Notes

- Make sure you have completed WhatsApp Web login once before running the script to avoid repeated QR code scans.
- This script is intended for educational or personal use and may need adjustments for reliability depending on Twitter or WhatsApp web UI changes.
- It uses hardcoded wait times; these may require tuning for different network conditions.
- Image downloads are temporarily saved as `tweet.jpg` in the script directory.

---
This tool provides a useful example of combining Selenium web automation with web scraping to perform cross-platform social media content distribution without official APIs.
