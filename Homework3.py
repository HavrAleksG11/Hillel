#alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


alice_in_wonderland = """Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don't "much care where" '——' said Alice.\n'
    '"Then it doesn't matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you're sure to do that," said the Cat, "if you only walk long enough."""
print(alice_in_wonderland)
for symbol in alice_in_wonderland:
    if symbol == "'":
        print(symbol)






"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""





# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""

black_sea_area_string = "436 402"
azov_sea_area_string = "37 800"
black_sea_area = int(black_sea_area_string.replace(" ", ""))
azov_sea_area = int(azov_sea_area_string.replace(" ", ""))
total_area = black_sea_area + azov_sea_area
print(f"Разом Чорне та Азовське моря займають {total_area:_}" .replace("_", " ") + "км2")



# task 05

"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

total_string = "375 291"
sklad_1_2_string = "250 449"
sklad_2_3_string = "222 950"
total = int(total_string.replace(" ", ""))
sklad_1_2 = int(sklad_1_2_string.replace(" ", ""))
sklad_2_3 = int(sklad_2_3_string.replace(" ", ""))
sklad_3 = total - sklad_1_2
sklad_1 = total - sklad_2_3
sklad_2 = sklad_1_2 - sklad_1
print(f"На першому складі:  {sklad_1:}".replace("_", " ") + " товарів")
print(f"На другому складі:  {sklad_2:}".replace("_", " ") + " товарів")
print(f"На третьому складі: {sklad_3:}".replace("_", " ") + " товарів")




# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

months = 1.5 * 12
monthly_payment = 1179
total_cost = months * monthly_payment
print(f"Вартість комп'ютера: {int(total_cost)} гривень")


# task 07

"""Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
print(a)
b = 9907 % 9
print(b)
c = 2789 % 5
print(c)
d = 7248 % 6
print(d)
e = 7128 % 5
print(e)
f = 19224 % 9
print(f)



# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

items_for_party = [
    {"name": "Піца велика", "quantity": 4, "price": 274},
    {"name": "Піца середня", "quantity": 2, "price": 218},
    {"name": "Сік", "quantity": 4, "price": 35},
    {"name": "Торт", "quantity": 1, "price": 350},
    {"name": "Вода", "quantity": 3, "price": 21}
]
total_sum = 0
for item in items_for_party:
    cost = item["quantity"] * item["price"]
    total_sum += cost
    print(f"{item['name']}: {item['quantity']} x {item['price']} = {cost} грн")
print(f"Загальна сума: {total_sum} грн")



# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
all_photos = 232
photos_on_page = 8
need_pages = all_photos // photos_on_page
print(f"Знадобиться {need_pages} сторінок ")




# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
tank_capacity = 48
consumption_per_100km = 9
total_fuel_needed = (distance / 100) * consumption_per_100km
print(f" Необхідно бензину: {int(total_fuel_needed)} літрів")
refuelings_during_trip = total_fuel_needed / tank_capacity
print(f"необхідно {int(refuelings_during_trip)} рази заїхати на заправку під час цієї подорожі")