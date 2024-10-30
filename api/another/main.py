import logging
import requests
from logger import setup_logging
from api_info_test import (
    test_api_info_contacts,
    test_api_info_delivery,
    test_api_info_returns,
    test_api_info_policy,
    test_api_info_register_policy,
    test_api_info_settings_acquirers,
    test_api_info_settings_globals,
    test_api_info_about
)

# Налаштовуємо логування
setup_logging()

# Функція для відправки повідомлень у Telegram
def send_to_telegram(message):
    bot_token = '7568161283:AAFfbo0mlQjllsgjvugA1ZfyyAhNY3vn1Ig'
    chat_id = '-1002491656470'
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    data = {'chat_id': chat_id, 'text': message}

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error(f"Помилка відправки повідомлення в Telegram: {e}")


# Запускаємо тести
if __name__ == '__main__':
    logging.info('=== START RUNNING TESTS ===')

    # Запускаємо кожен тест в окремому блокові try/except
    try:
        test_api_info_contacts()
    except Exception as e:
        logging.error(f"Test test_api_info_contacts failed: {str(e)}")

    try:
        test_api_info_delivery()
    except Exception as e:
        logging.error(f"Test test_api_info_delivery failed: {str(e)}")

    try:
        test_api_info_returns()
    except Exception as e:
        logging.error(f"Test test_api_info_returns failed: {str(e)}")

    try:
        test_api_info_policy()
    except Exception as e:
        logging.error(f"Test test_api_info_policy failed: {str(e)}")

    try:
        test_api_info_register_policy()
    except Exception as e:
        logging.error(f"Test test_api_info_register_policy failed: {str(e)}")

    try:
        test_api_info_settings_acquirers()
    except Exception as e:
        logging.error(f"Test test_api_info_settings_acquirers failed: {str(e)}")

    try:
        test_api_info_settings_globals()
    except Exception as e:
        logging.error(f"Test test_api_info_settings_globals failed: {str(e)}")

    try:
        test_api_info_about()
    except Exception as e:
        logging.error(f"Test test_api_info_about failed: {str(e)}")

    logging.info('=== FINISH RUNNING THE TESTS ===')

with open('api_tests_fail.log', 'r') as file:
    lines = file.readlines()
    if lines:
        last_error = lines[-1]  # Отримання останнього запису з логу
        send_to_telegram(last_error)


