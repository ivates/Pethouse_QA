import logging
import requests
from logger import setup_logging ###

# # Налаштування логування
# setup_logging()
# logger = logging.getLogger()
#
# base_url = 'https://pethouse.ua'
# language = '/app/v1/ua'
#
# def log_request_and_response(response, endpoint):
#     logger.info(f"Testing endpoint: {endpoint}")
#     logger.info(f"Status code: {response.status_code}")
#     logger.info(f"Headers: {response.headers}")
#     logger.info(f"Response body: {response.json()}")


# Налаштування логування
setup_logging()
logger = logging.getLogger()

base_url = 'https://pethouse.ua'
language = '/app/v1/ua'

def log_request_and_response(response, endpoint):
    logger.info(f"Testing endpoint: {endpoint}")
    logger.info(f"Status code: {response.status_code}")
    logger.info(f"Headers: {response.headers}")
    logger.info(f"Response body: {response.json()}")

# Функція для запуску тестів і збору результатів
def run_tests():
    test_results = []

    # Викликати тести і збирати результати
    test_results.append(run_test(test_api_info_contacts))
    test_results.append(run_test(test_api_info_delivery))
    test_results.append(run_test(test_api_info_returns))
    test_results.append(run_test(test_api_info_policy))
    test_results.append(run_test(test_api_info_register_policy))
    test_results.append(run_test(test_api_info_settings_acquirers))
    test_results.append(run_test(test_api_info_settings_globals))

    # Підсумковий звіт
    for result in test_results:
        logger.info(result)

def run_test(test_function):
    try:
        test_function()
        return f"{test_function.__name__}: PASSED"
    except AssertionError as e:
        logger.error(f"Critical failure in {test_function.__name__}: {e}")
        return f"{test_function.__name__}: FAILED"
    except Exception as e:
        logger.error(f"Unexpected error in {test_function.__name__}: {e}")
        return f"{test_function.__name__}: ERROR"


#СТОРІНКА КОНТАКТІВ
def test_api_info_contacts():
    endpoint = '/info/contacts/'
    full_url = base_url + language + endpoint


    # Виконуємо GET-запит до API
    response = requests.get(full_url, headers = {'accept': 'application/json'})

    # Налаштовуємо логування
    log_request_and_response(response, endpoint)

    # Перевіряємо статус-код відповіді
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # Перевіряємо заголовки відповіді
    assert response.headers['content-type'] == 'application/json; charset=UTF-8', "Wrong content type"

    # Перевіряємо, чи є заголовок 'cache-control' у відповіді
    if 'cache-control' in response.headers:
        # Перевіряємо кешування (допускаємо кілька варіантів)
        expected_cache_controls = ['no-cache', 'private, must-revalidate']
        assert any(option in response.headers['cache-control'] for option in expected_cache_controls), \
            f"Unexpected cache control. Got {response.headers['cache-control']}"
    else:
        # Якщо заголовка немає, виводимо повідомлення про це
        logging.warning("Warning: 'cache-control' header is missing in the response")

    # Тіло відповіді в форматі JSON
    data = response.json()

    # Перевіряємо структуру відповіді
    expected_structure = {
        "work-time": int,
        "phone": str,
        "phone-comment": str,
        "callback-title": str,
        "mail": str,
        "messenger-title": str,
        "messengers": dict
    }

    for key, expected_type in expected_structure.items():
        assert key in data, f"Key '{key}' is missing in the response"
        assert isinstance(data[key], expected_type), f"Key '{key}' is of wrong type. Expected {expected_type}, got {type(data[key])}"

    # Перевіряємо внутрішню структуру 'messengers'
    expected_messengers_structure = {
        "viber": str,
        "telegram": str,
        "fb": str
    }

    messengers = data["messengers"]
    for key, expected_type in expected_messengers_structure.items():
        assert key in messengers, f"Key '{key}' is missing in 'messengers'"
        assert isinstance(messengers[key], expected_type), f"Key '{key}' in 'messengers' is of wrong type. Expected {expected_type}, got {type(messengers[key])}"


#СТОРІНКА ОПЛАТА І ДОСТАВКА
def test_api_info_delivery():
    endpoint = '/info/delivery/'
    full_url = base_url + language + endpoint


    # Виконуємо GET-запит до API
    response = requests.get(full_url, headers={'accept': 'application/json'})

    # Налаштовуємо логування
    log_request_and_response(response, endpoint)


    # Перевіряємо статус-код відповіді
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # Перевіряємо заголовки відповіді
    assert response.headers['content-type'] == 'application/json; charset=UTF-8', "Wrong content type"

    # Перевіряємо, чи є заголовок 'cache-control' у відповіді
    if 'cache-control' in response.headers:
        # Перевіряємо кешування (допускаємо кілька варіантів)
        expected_cache_controls = ['no-cache', 'private, must-revalidate']
        assert any(option in response.headers['cache-control'] for option in expected_cache_controls), \
            f"Unexpected cache control. Got {response.headers['cache-control']}"
    else:
        # Якщо заголовка немає, виводимо повідомлення про це
        logging.warning("Warning: 'cache-control' header is missing in the response")


    # Тіло відповіді в форматі JSON
    data = response.json()

    # Перевіряємо структуру відповіді
    expected_structure = {
        "title": str,
        "data": str
    }

    for key, expected_type in expected_structure.items():
        assert key in data, f"Key '{key}' is missing in the response"
        assert isinstance(data[key], expected_type), f"Key '{key}' is of wrong type. Expected {expected_type}, got {type(data[key])}"




#СТОРІНКА ОБМІН ТА ПОВЕРНЕННЯ ТОВАРІВ
def test_api_info_returns():
    endpoint = '/info/returns/'
    full_url = base_url + language + endpoint


    # Виконуємо GET-запит до API
    response = requests.get(full_url, headers={'accept': 'application/json'})

    log_request_and_response(response, endpoint)#####

    #Перевірка статус-код відповіді
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    #Перевіряємо заголовки відповіді
    assert response.headers['content-type'] == 'application/json; charset=UTF-8', "Wrong content type"

    # Перевіряємо, чи є заголовок 'cache-control' у відповіді
    if 'cache-control' in response.headers:
        # Перевіряємо кешування (допускаємо кілька варіантів)
        expected_cache_controls = ['no-cache', 'private, must-revalidate']
        assert any(option in response.headers['cache-control'] for option in expected_cache_controls), \
            f"Unexpected cache control. Got {response.headers['cache-control']}"
    else:
        # Якщо заголовка немає, виводимо повідомлення про це
        logging.warning("Warning: 'cache-control' header is missing in the response")

    #Тіло відповіді в форматі JSON
    data = response.json()

    #Перевіряємо структуру відповіді
    expected_structure = {
        "title": str,
        "data": str
    }

    for key, expected_type in expected_structure.items():
        assert key in data, f"Key '{key}' is missing in the response"
        assert isinstance(data[key], expected_type), f"Key '{key}' is of wrong type. Expected {expected_type}, got {type(data[key])}"



# СТОРІНКА ПОЛІТИКИ КОНФІДЕНЦІЙНОСТІ
def test_api_info_policy():
    endpoint = '/info/policy/'
    full_url = base_url + language + endpoint


    # Виконуємо GET-запит до API
    response = requests.get(full_url, headers={'accept': 'application/json'})

    # Налаштовуємо логування
    log_request_and_response(response, endpoint)

    # Перевірка статус-коду відповіді
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # Перевіряємо, чи є заголовок 'cache-control' у відповіді
    if 'cache-control' in response.headers:
        # Перевіряємо кешування (допускаємо кілька варіантів)
        expected_cache_controls = ['no-cache', 'private, must-revalidate']
        assert any(option in response.headers['cache-control'] for option in expected_cache_controls), \
            f"Unexpected cache control. Got {response.headers['cache-control']}"
    else:
        # Якщо заголовка немає, виводимо повідомлення про це
        logging.warning("Warning: 'cache-control' header is missing in the response")

    # Тіло відповіді
    data = response.json()

    # Перевіряємо структуру відповіді
    expected_structure = {
        "title": str,
        "data": str
    }

    for key, expected_type in expected_structure.items():
        assert key in data, f"Key '{key}' is missing in the response"
        assert isinstance(data[key], expected_type), f"Key '{key}' is of wrong type. Expected {expected_type}, got {type(data[key])}"




# СТОРІНКА ДИСКОНТНА ПРОГРАМА
def test_api_info_register_policy():
    endpoint = '/info/register-policy/'
    full_url = base_url + language + endpoint


    # Виконуємо GET-запит до API
    response = requests.get(full_url, headers={'accept': 'application/json'})

    # Налаштовуємо логування
    log_request_and_response(response, endpoint)

    #Перевірка статус-коду відповіді
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    #Перевіряємо, чи є заголовок 'cache-control' у відповіді
    if 'cache-control' in response.headers:
        #Перевіряємо кешування (допускаємо кілька варіантів)
        expected_cache_controls = ['no-cache', 'private, must-revalidate']
        assert any(option in response.headers['cache-control'] for option in expected_cache_controls), \
            f"Unexpected cache control. Got {response.headers['cache-control']}"

    else:
        #Якщо заголовка немає, виводимо повідомлення про це
        logging.warning("Warning: 'cache-control' headers is missing in the response")


    #Тіло відповіді
    data =  response.json()

    #Перевіряємо структуру відповіді
    expected_structure = {
        "title": str,
        "data": str
    }

    for key, expected_type in expected_structure.items():
        assert key in data, f"Key '{key}' is missing in the response"
        assert isinstance(data[key], expected_type), f"Key '{key}' is of wrong type. Expected {expected_type}, got {type(data[key])}"



# СТОРІНКА ДОСТУПНІ БАНКИ-ЕКВАЄРИ
def test_api_info_settings_acquirers():
    endpoint = '/settings/acquirers/'
    full_url = base_url + language + endpoint

    # Виконуємо GET-запит до API
    response = requests.get(full_url, headers={'accept': 'application/json'})

    # Налаштовуємо логування
    log_request_and_response(response, endpoint)

    #Перевірка статус-коду відповіді
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    #Перевіряємо, чи є заголовок 'cache-control' у відповіді
    if 'cache-control' in response.headers:
        #Перевіряємо кешування (допускаємо кілька варіантів)
        expected_cache_controls = ['no-cache', 'private, must-revalidate']
        assert any(option in response.headers['cache-control'] for option in expected_cache_controls), \
            f"Unexpected cache control. Got {response.headers['cache-control']}"

    else:
        #Якщо заголовка немає, виводимо повідомлення про це
        logging.warning("Warning: 'cache-control' headers is missing in the response")


    #Тіло відповіді
    data =  response.json()

    #Перевіряємо що відповідь є списком
    assert isinstance(data, list), f"Expected response to be a list, but got {type(data)}"

    #Перевіряємо структуру відповіді
    expected_structure = {
        "acquirer": str,
        "active": int
    }

    for item in data:
        for key, expected_type in expected_structure.items():
            assert key in item, f"Key '{key}' is missing in one of the items"
            assert isinstance(item[key],
                                expected_type), f"Key '{key}' is of wrong type. Expected {expected_type}, got {type(item[key])}"



# СТОРІНКА ДОСТУПНІ БАНКИ-ЕКВАЄРИ
def test_api_info_settings_globals():
    endpoint = '/settings/globals/'
    full_url = base_url + language + endpoint

    # Виконуємо GET-запит до API
    response = requests.get(full_url, headers={'accept': 'application/json'})

    # Налаштовуємо логування
    log_request_and_response(response, endpoint)

    #Перевірка статус-коду відповіді
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    #Перевіряємо, чи є заголовок 'cache-control' у відповіді
    if 'cache-control' in response.headers:
        #Перевіряємо кешування (допускаємо кілька варіантів)
        expected_cache_controls = ['no-cache', 'private, must-revalidate']
        assert any(option in response.headers['cache-control'] for option in expected_cache_controls), \
            f"Unexpected cache control. Got {response.headers['cache-control']}"

    else:
        #Якщо заголовка немає, виводимо повідомлення про це
        logging.warning("Warning: 'cache-control' headers is missing in the response")


    #Тіло відповіді
    data =  response.json()

    #Перевіряємо що відповідь є списком
    assert isinstance(data, list), f"Expected response to be a list, but got {type(data)}"

    #Перевіряємо структуру відповіді
    expected_structure = {
        "setting": str,
        "value": int
    }

    for item in data:
        for key, expected_type in expected_structure.items():
            assert key in item, f"Key '{key}' is missing in one of the items"
            assert isinstance(item[key],
                                expected_type), f"Key '{key}' is of wrong type. Expected {expected_type}, got {type(item[key])}"






# СТОРІНКА ПРО КОМПАНІЮ
def test_api_info_about():
    endpoint = '/info/about/'
    full_url = base_url + language + endpoint

    # Виконуємо GET-запит до API
    response = requests.get(full_url, headers={'accept': 'application/json'})

    # Налаштовуємо логування
    log_request_and_response(response, endpoint)

    #Перевірка статус-коду відповіді
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    #Перевіряємо, чи є заголовок 'cache-control' у відповіді
    if 'cache-control' in response.headers:
        #Перевіряємо кешування (допускаємо кілька варіантів)
        expected_cache_controls = ['no-cache', 'private, must-revalidate']
        assert any(option in response.headers['cache-control'] for option in expected_cache_controls), \
            f"Unexpected cache control. Got {response.headers['cache-control']}"

    else:
        #Якщо заголовка немає, виводимо повідомлення про це
        logging.warning("Warning: 'cache-control' headers is missing in the response")

    #Тіло відповіді
    data =  response.json()

    #Перевіряємо структуру відповіді
    expected_structure = {
        "title": str,
        "data": type(None)
    }

    for key, expected_type in expected_structure.items():
            assert key in data, f"Key '{key}' is missing in the response"
            assert isinstance(data[key], expected_type), f"Key '{key}' is of wrong type. Expected {expected_type}, got {type(data[key])}"



