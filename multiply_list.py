import random

def multiply_list():
    numbers_list = []

    #Generate a random list to do exercises on each time
    for i in range(0, 25):
        x = random.randint(-100, 100)
        numbers_list.append(x)
    print('Your random list is: ')
    print(numbers_list)
    print()

    #Multiply a list
    factor = random.randint(1, 5)
    multiplied_list = []
    print('The multiplication factor is %d:' % (factor))

    for t in range(len(numbers_list)):
        z = numbers_list[t] * factor
        multiplied_list.append(z)
    print(multiplied_list)
    return