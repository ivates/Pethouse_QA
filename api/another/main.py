# import logging
# from logger import setup_logging
# from api_info_test import (
#     test_api_info_contacts,
#     test_api_info_delivery,
#     test_api_info_returns,
#     test_api_info_policy,
#     test_api_info_register_policy,
#     test_api_info_settings_acquirers,
#     test_api_info_settings_globals,
#     test_api_info_about
# )
#
# # Налаштовуємо логування
# setup_logging()
#
# # Запускаємо тести
# if __name__ == '__main__':
#     logging.info('=== START RUNNING TESTS ===')
#     test_api_info_contacts()
#     test_api_info_delivery()
#     test_api_info_returns()
#     test_api_info_policy()
#     test_api_info_register_policy()
#     test_api_info_settings_acquirers()
#     test_api_info_settings_globals()
#     test_api_info_about()
#
#
#     logging.info('===  FINISH RUNNING THE TESTS ===')


import logging
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
