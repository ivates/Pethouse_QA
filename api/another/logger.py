import logging


def setup_logging():
    # Отримуємо root-логер
    root_logger = logging.getLogger()

    # Видаляємо всі існуючі обробники, щоб уникнути дублювання
    if root_logger.hasHandlers():
        root_logger.handlers.clear()

    # Налаштовуємо основний лог-файл для запису всіх рівнів логів
    logging.basicConfig(
        filename='api_tests.log',
        level=logging.DEBUG,  # Записуємо всі повідомлення рівня DEBUG і вище
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    # Налаштовуємо окремий лог-файл для помилок (FAIL)
    error_handler = logging.FileHandler('api_tests_fail.log')
    error_handler.setLevel(logging.ERROR)  # Записуємо лише помилки рівня ERROR і вище
    error_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    # Додаємо обробник помилок до root-логера
    root_logger.addHandler(error_handler)

    logging.info('LOGGING IS SET UP SUCCESSFULLY')  # Повідомлення про успішне налаштування логування


# Виклик функції для налаштування логування
setup_logging()

# # logger.py
# import logging
#
# def setup_logging():
#     # Налаштовуємо основний лог-файл для запису всіх рівнів логів
#     logging.basicConfig(
#         filename='api_tests.log',
#         level=logging.DEBUG,  # Записуємо всі повідомлення рівня DEBUG і вище
#         format='%(asctime)s - %(levelname)s - %(message)s'
#     )
#
#     # Налаштовуємо окремий лог-файл для помилок (FAIL)
#     error_handler = logging.FileHandler('api_tests_fail.log')
#     error_handler.setLevel(logging.ERROR)  # Записуємо лише помилки рівня ERROR і вище
#     error_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
#
#     # Додаємо обробник помилок до root-логера
#     root_logger = logging.getLogger()
#     root_logger.addHandler(error_handler)
#
#     logging.info('LOGGING IS SET UP SUCCESSFULLY')  # Повідомлення про успішне налаштування логування
#
# # Виклик функції для налаштування логування
# setup_logging()
