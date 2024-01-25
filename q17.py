# 17. Write a program that serves as a basic calculator. It asks for two
# numbers, then it asks for an operator. Gracefully deal with input that
# doesn't cleanly convert to numbers. Deal with division by zero errors.

try:
    number1 = int(input("Enter number1: "))
except ValueError:
    print("Can't convert the input to int")
    exit()
try:
    number2 = int(input("Enter number2: "))
except ValueError:
    print("Can't convert the input to int")
    exit()

number3 = input("Enter the operator: ")

match(number3):
    case "+":
         print(number1 + number2)
    case "*":
         print(number1 * number2)
    case "-":
         print(number1 - number2)
    case "/":
        try:
             print(number1 / number2)
        except ZeroDivisionError:
            print("Cant divide by zero")
    case _:
        print("Invalid operator")

# print(result)

