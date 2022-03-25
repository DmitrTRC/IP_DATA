# file_name = input("Enter file name: ")
# try:
#     with open(file_name) as fd:
#         for line in fd:
#             print(line, end='\n')
# except FileNotFoundError:
#     print("File not found")
# else:
#     print("File found")
# finally:
#     print("File processing done")


def divider(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Division by zero is not allowed")
    else:
        print(result)


def divider2(num1, num2):
    if num2 == 0:
        print("You cannot divide by zero")
    else:
        print(num1 / num2)


divider(10, 0)
divider(10, 2)
divider2(10, 0)
