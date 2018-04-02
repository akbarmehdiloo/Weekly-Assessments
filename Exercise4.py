
# Akbar Mehdiloo

def a (number):
    for i in range(1, 21):
        if number % i != 0:
            return False
    return True
number = 1
while True:
    if a (number):
        break
    number += 1   
print(number)

# The answer is 232792560
