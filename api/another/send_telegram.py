import requests

TOKEN = '7568161283:AAFfbo0mlQjllsgjvugA1ZfyyAhNY3vn1Ig'
CHAT_ID = '543824111'
LOG_FILE = 'api_tests_fail.log'

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

def send_error_log():
    with open(LOG_FILE, 'r') as file:
        log_content = file.read()
        if log_content:
            send_telegram_message("Errors found in API tests:\n" + log_content)

if __name__ == "__main__":
    send_error_log()
