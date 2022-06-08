Marks = int(input('Marks you obtained:\n\t'))
if Marks <= 50:
    if Marks < 25:
        print('Your grade is F grade')
    else:
        if Marks < 45:
            print('You got E grade')
        else:
            print('You got D grade')
else:
    if Marks < 60:
        print('You got C grade')
    else:
        if Marks < 80:
            print('You got B grade')
        else:
            print('You got A grade!')




year = int(input('Enter year: \n\t'))
a = year % 4
b = year % 100
c = year % 400
if a == 0:
    if b == 0:
        if c == 0:
            print('The year is a leap year!')
        else:
            print('The year is not a leap year')
    else:
        print('The year is a leap year!')
else:
    print('The year is not a leap year')




from random import randint

for i in range(1, 11):
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    print(f" ques {i} --> {num1}x{num2}")
    a = int(input('Enter answer of ques 1:'))
    if a == num1 * num2:
        print('Right !')
    else:
        print(f'Wrong, answer is {num1 * num2}')




x = 200
for i in range(x):
    if i % 5 == 2:
        if i % 6 == 3:
            if i % 7 == 2:
                print(i, 'candies are in the bowl!')
