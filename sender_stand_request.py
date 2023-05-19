import configuration
import requests
import data

def post_new_order(order_body): # создание нового заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,  # подставялем полный url
                     json=order_body,  # тут тело
                     headers=data.headers)  # а здесь заголовки

def get_order_token():  # выдергиваем значение track из созданного заказа
    order_body = data.order_body.copy()
    res = post_new_order(order_body)
    track = res.json()["track"]
    return track

def get_order():   # получение из базы заказа по track номеру
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + str(get_order_token()))  # подставялем полный url
