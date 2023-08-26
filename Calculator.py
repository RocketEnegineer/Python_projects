print("Calculator")

def calculate_function(a, b, c):
    if a == "+":
        return numb_1 + numb_2
    elif a == "-":
        return numb_1 - numb_2
    elif a == "*":
         return numb_1 * numb_2
    elif a == ":":
        return numb_1 / numb_2
    elif a == "%":
        return numb_1 % numb_2

numb_1 = int(input("Enter first number: "))
numb_2 = int(input("Enter second number: "))

operator = input("Chose  operator: +, -, :, *, %: ")

print(str(numb_1), operator, str(numb_2), "=", str(calculate_function(operator, numb_1, numb_2)))


