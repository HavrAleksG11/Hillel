data = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]


def sum_of_numbers(s):
    try:
        numbers = [int(x) for x in s.split(",")]
        return sum(numbers)
    except ValueError:
        return "Не можу це зробити!"


for item in data:
    print(sum_of_numbers(item))
