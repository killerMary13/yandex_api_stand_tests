import sender_stand_request
import data

# Функция меняющая содержимое тела запроса для корзины
def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body

# Функция для позитивной проверки
def positive_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_create_kit_new_user(kit_body)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name

# Функция негативной проверки
def negative_assert(kit_body):
    kit_response = sender_stand_request.post_create_kit_new_user(kit_body)
    assert kit_response.status_code == 400 or 500

# Тест 1. Допустимое количество символов (1):
def test_create_kit_name_with_1_symbol():
    positive_assert("a")

# Тест 2. Допустимое количество символов (511):
def test_create_kit_name_with_max_symbols():
    positive_assert(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Тест 3. Количество символов меньше допустимого (0):
def test_create_kit_name_with_0_symbols():
    negative_assert("")

# Тест 4. Количество символов больше допустимого (512):
def test_create_kit_name_with_more_max_symbols():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Тест 5. Разрешены английские буквы:
def test_create_kit_name_with_en_symbols():
    positive_assert("QWErty")

# Тест 6. Разрешены русские буквы:
def test_create_kit_name_with_rus_symbols():
    positive_assert("Мария")

# Тест 7. Разрешены спец.символы:
def test_create_kit_name_with_symbols():
    positive_assert("\"№%@\",\"")

# Тест 8. Разрешены пробелы:
def test_create_kit_name_with_white_spaces():
    positive_assert(" Человек и КО ")

# Тест 9. Разрешены цифры:
def test_create_kit_name_with_number():
    positive_assert("123")

# Тест 10. Параметр не передан в запросе:
def test_create_kit_name_none():
    current_kit_body_name_none = data.kit_body.copy()
    current_kit_body_name_none.pop("name")
    negative_assert(current_kit_body_name_none)

# Тест 11. Передан другой тип параметра (число):
def test_create_kit_with_invalide_type():
    negative_assert(123)