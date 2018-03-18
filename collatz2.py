# Akbar Mehdiloo (I tried to do this myself but it looks like it didn't work)
# for this reason I had a look at the below link to solve this problem. 
https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff
x = int(input("Please give me a number")
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result
while n != 1:
    n = collatz(int(n))

