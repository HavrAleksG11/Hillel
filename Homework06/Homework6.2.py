while True:
    word = input("Введіть слово, яке містить літеру 'h': ")
    if "h" in word.lower():
        print("Дякую! Ви ввели правильне слово:", word)
        break
    else:
        print("У слові немає літери 'h'. Спробуйте ще раз.")
