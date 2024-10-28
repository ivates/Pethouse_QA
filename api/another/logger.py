import logging


def setup_logging():
    # �������� root-�����
    root_logger = logging.getLogger()

    # ��������� �� ������� ���������, ��� �������� ����������
    if root_logger.hasHandlers():
        root_logger.handlers.clear()

    # ����������� �������� ���-���� ��� ������ ��� ���� ����
    logging.basicConfig(
        filename='api_tests.log',
        level=logging.DEBUG,  # �������� �� ����������� ���� DEBUG � ����
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    # ����������� ������� ���-���� ��� ������� (FAIL)
    error_handler = logging.FileHandler('api_tests_fail.log')
    error_handler.setLevel(logging.ERROR)  # �������� ���� ������� ���� ERROR � ����
    error_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    # ������ �������� ������� �� root-������
    root_logger.addHandler(error_handler)

    logging.info('LOGGING IS SET UP SUCCESSFULLY')  # ����������� ��� ������ ������������ ���������


# ������ ������� ��� ������������ ���������
setup_logging()

# # logger.py
# import logging
#
# def setup_logging():
#     # ����������� �������� ���-���� ��� ������ ��� ���� ����
#     logging.basicConfig(
#         filename='api_tests.log',
#         level=logging.DEBUG,  # �������� �� ����������� ���� DEBUG � ����
#         format='%(asctime)s - %(levelname)s - %(message)s'
#     )
#
#     # ����������� ������� ���-���� ��� ������� (FAIL)
#     error_handler = logging.FileHandler('api_tests_fail.log')
#     error_handler.setLevel(logging.ERROR)  # �������� ���� ������� ���� ERROR � ����
#     error_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
#
#     # ������ �������� ������� �� root-������
#     root_logger = logging.getLogger()
#     root_logger.addHandler(error_handler)
#
#     logging.info('LOGGING IS SET UP SUCCESSFULLY')  # ����������� ��� ������ ������������ ���������
#
# # ������ ������� ��� ������������ ���������
# setup_logging()
