# Telegram Contract Monitor

This script monitors specified Telegram groups for Solana contract addresses and forwards them to a bot if they meet certain criteria.

## Features
- Monitors messages in up to 4 Telegram groups.
- Detects Solana contract addresses via regex.
- Forwards addresses to a specified bot if certain conditions are met.

## Requirements
- Python 3.8 or higher
- Telegram API credentials (get yours from https://my.telegram.org)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/telegram-contract-monitor.git
   cd telegram-contract-monitor

2. Install the required dependencies:

   pip install -r requirements.txt

Setup

1. Obtain your Telegram api_id and api_hash:

Visit Telegram's API page and log in.  https://my.telegram.org/auth
Create a new app and note down the api_id and api_hash.
Edit monitor.py:

2. Replace YOUR_API_ID, YOUR_API_HASH, YOUR_BOT_USERNAME, and group IDs with your own details. （https://web.telegram.org/a/  Click on the conversation channel on the web page. The number at the top of the web page is the channel group ID -100）

3. (Optional) Add a persistent record file: If you want to retain contract data between sessions, ensure the file contract_records.json is present in the same directory.

Usage

Run the script:

python monitor.py


Contributing

Contributions are welcome! Please open an issue or submit a pull request.