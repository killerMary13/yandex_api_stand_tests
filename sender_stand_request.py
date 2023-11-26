import configuration
import requests
import data

# Создание нового пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

# Сохранение токена пользователя
data.headers_AuthToken["Authorization"] = "Bearer " + str(response.json()['authToken'])
print(data.headers_AuthToken)

def post_create_kit_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.MAIN_KITS,
                         headers=data.headers_AuthToken,
                         json=body)
response = post_create_kit_new_user(data.kit_body)
print(response.status_code)
print(response.json())