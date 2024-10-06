import random

print('Guess a number! Simple game')
num = random.randint(1,31)
num_inp = int(input('Please enter a number between 1-30 :'))


if num_inp == num :
    print('YOU WIN!!!!!!!!!!!!!!!!!😎😎😎😎😎😎😎😎😎😎😎😎')
else:
    print('bruh you are wrong💀💀💀💀💀💀💀💀💀💀💀')
    print('The number is : ',num)
