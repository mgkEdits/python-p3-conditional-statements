#!/usr/bin/env python3

def admin_login(username, password):
    if (username.upper() == "ADMIN" and password == "12345"):
        return "Access granted"
    else:
        return "Access denied"
    pass

def hows_the_weather(temperature):
    if temperature < 40:
        response = "brisk"
    elif 40 <= temperature <= 65:
        response = "a little chilly"
    elif temperature > 85:
        response = "too dang hot"
    else:
        response = "perfect"
    return f"It's {response} out there!"
    pass

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
    pass

def calculator(operation, num1, num2):
    if operation in ["+", "-", "*", "/"]:
        return eval(f"{num1} {operation} {num2}")
    else:
        print("Invalid operation!")
        return None
    pass
