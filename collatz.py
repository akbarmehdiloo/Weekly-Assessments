# Akbar Mehdiloo 

number = input("Please any number you wish: ")
while number != 1: 
    if number % 2 == 0:
        print(number // 2)
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
