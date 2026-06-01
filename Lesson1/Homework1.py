 # task 01 == Виправте синтаксичні помилки
print("Hello", end=" ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук

apples = 2
banana = 4 * apples
print(banana)

# task 05 == виправте назви змінних#

storona = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача

perimetery = _storona + storona_2 + storona_3 + storona_4
print(perimetery)

"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07

"""У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?"""

apple = 4
grusha = 5 + apple
sliva = apple - 2
all_trees = apple + grusha + sliva
print("In garden ", all_trees, "trees")

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""

do_obida = 5
pislia_obida = do_obida - 10
nadvechir = pislia_obida + 4
print("Temperatura nadvechir", nadvechir, "gradusiv")

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""

boys = 24
girls = 24 / 2
sick_boys = boys - 1
absent_today_girls = girls - 2
all_children = int(sick_boys + absent_today_girls)
print("V Gurtku today", all_children, )

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
first_book = 8
second_book = first_book + 2
third_book = (first_book + second_book) / 2
all_books = first_book + second_book + third_book
print("Vsi razom books coast", int(all_books), "grivni", ",", "first book coast", int(first_book), "second book coast",
      int(second_book), "third book coast", int(third_book))
