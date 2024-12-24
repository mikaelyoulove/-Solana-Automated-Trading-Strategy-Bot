from telethon import TelegramClient, events
import re
import json

# Telegram API configuration
api_id = 'YOUR_API_ID'  # Replace with your actual api_id
api_hash = 'YOUR_API_HASH'  # Replace with your actual api_hash
bot_username = 'YOUR_BOT_USERNAME'  # Replace with your target bot username

# Monitored groups
groups = {
    -1000000000000: 'A',  # Replace with actual group ID
    -1000000000001: 'B',  # Replace with actual group ID
    -1000000000002: 'C',  # Replace with actual group ID
    -1000000000003: 'D'   # Replace with actual group ID
}

# Contract records {contract_address: {'first_seen': 'A', 'forwarded': False}}
contract_records = {}

# Persistent record file
record_file = 'contract_records.json'

# Regex to match Solana contract addresses
solana_contract_pattern = re.compile(r'[1-9A-HJ-NP-Za-km-z]{32,44}')

# Load records from file
def load_records():
    try:
        with open(record_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("No record file found, initializing empty records.")
        return {}

# Save records to file
def save_records():
    try:
        with open(record_file, 'w') as f:
            json.dump(contract_records, f, indent=2)
        print("Records saved successfully.")
    except Exception as e:
        print(f"Error saving records: {e}")

# Initialize Telegram client
client = TelegramClient('session_name', api_id, api_hash)

# Load historical records
contract_records = load_records()

@client.on(events.NewMessage(chats=list(groups.keys())))
async def handle_message(event):
    global contract_records

    group_id = event.chat_id  # Current message's group ID
    group_tag = groups.get(group_id, None)  # Corresponding tag for the group (A, B, C, D)
    if not group_tag:
        return

    message_text = event.message.message
    matches = solana_contract_pattern.findall(message_text)  # Find contract addresses

    for address in matches:
        if address not in contract_records:
            # First time recording the contract address
            contract_records[address] = {'first_seen': group_tag, 'forwarded': False}
            print(f"First recorded contract {address} in group {group_tag}")
        else:
            # Check if forwarding is needed
            first_seen = contract_records[address]['first_seen']
            if group_tag != first_seen and not contract_records[address]['forwarded']:
                try:
                    # Forward to the bot
                    await client.send_message(bot_username, f"Contract Address: {address}")
                    contract_records[address]['forwarded'] = True
                    print(f"Forwarded contract address {address}, first seen in {first_seen}, now from {group_tag}")
                except Exception as e:
                    print(f"Forwarding failed: {e}")

    save_records()

print("Script is running...")

# Start listening
with client:
    client.run_until_disconnected()
