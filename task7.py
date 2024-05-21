#Задача 7_1
month = 15
spring_months = [3, 4, 5]
summer_months = [6, 7, 8]
autumn_months = [9, 10, 11]
winter_months = [12, 1, 2]
if month in spring_months:
    print("Весна")
elif month in summer_months:
    print("Лето")
elif month in autumn_months:
    print("Осень")
elif month in winter_months:
    print("Зима")
else:
    print("Некорректный номер месяца")

#Задача 7_2
is_logged_in = True
has_shipping_adress = True
has_items_in_cart = False

has_order = False
if is_logged_in and has_shipping_adress and has_items_in_cart:
    print("Все критерии для оформления заказа выполнены. Заказ может быть оформлен")
    has_order = True
    print("Все критерии для оформления заказа выполнены. Пожалуйста, проверьте информацию")

min_purchase_for_discoint =1000
total_purchase = 1500
is_first_order = False

if is_first_order or total_purchase >= min_purchase_for_discoint:
    print("Вы получаете скидку!")

#Задача 7_3
check = [7, 13, 21]
number = int(input('Введите число -> '))
if number in check:
    print('Счастливое число!')
elif number > 0 and number <= 100:
    print('Число в диапазоне')
else:
    print('Не повезло(((((')
