import data
import sender_stand_request

# Функция для позитивной проверки
def positive_assert():
    # В переменную response сохраняется результат ответа сервера на поиск по track номеру:
    response = sender_stand_request.get_order()
    # Проверяется, что код ответа равен 200
    assert response.status_code == 200

def test_get_code():
   positive_assert()

