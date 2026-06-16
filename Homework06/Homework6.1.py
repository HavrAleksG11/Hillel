text = input("Some text: ")

unique_count = len(set(text))

if unique_count > 10:
    print(True)
else:
    print(False)
