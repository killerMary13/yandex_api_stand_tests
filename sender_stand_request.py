import configuration
import requests
import data

# Создание нового пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

# Создание набора
def post_create_kit_new_user(body):
    response = post_new_user(data.user_body)
    data.headers["Authorization"] = "Bearer " + str(response.json()['authToken'])
    return requests.post(configuration.URL_SERVICE + configuration.MAIN_KITS,
                         headers=data.headers,
                         json=body)