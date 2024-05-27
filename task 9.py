
student_scores = {
 "Маша": 85,
 "Саша": 92,
 "Петя": 78
}
print(student_scores["Маша"]) # Выводит 85
print(student_scores["Саша"]) # Выводит 92


list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл"]
print('первый учатник:', list_players[0], '\nвторой участник:', list_players[-1])


shopping_list = ["яблоко", "молоко", "хлеб", "яблоко", "масло", "яйца", "молоко"]
unique_items = set(shopping_list)
print("Количество уникальных товаров:", len(unique_items))


users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
print('уникальные входы:', print(len([i for i in enumerate(sorted(users)) if i[0] == 0 or i[1] != sorted(users)[i[0] - 1]])))
print('все входы:', len(users))

name = "Ваше имя"
age = 25
print(f"Привет, меня зовут {name} и мне {age} лет.")
x = 1695
y = 3305
print(f"Сумма чисел {x} и {y} равна {x + y}.")
number = 3.14159
print(f"Число Пи: {number:.2f}")