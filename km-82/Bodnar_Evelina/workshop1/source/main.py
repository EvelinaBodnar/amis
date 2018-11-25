"""
1.Катети прямокутного трикутника уводяться з клавіатури. Обчислити довжину гіпотенузи, периметр і площу цього трикутника.
 Відповідь дати з точністю до 10 знаків після коми.
2.Увести з клавіатури величини двох кутів трикутника (в градусах). Визначити, чи існує такий трикутник, і якщо так, то чи
 буде він прямокутним.
3.F(x)=9,якщо x<=-3
  F(x)=1/(x**2 + 1),якщо x>-3
"""



from math import *

def first_task():
    '''
    Functions that will be used in labs (або інший короткий опис файлу)
    File:lab_1.py
        Ця функція знаходить гіпотенузу(при умові,що він прямокутний),периметр та площу
        Args:
    	    a:  float.number
    		b:  float.number
    	Returns:
    	    A float number is the result
    	Exceptions:
    	    >>>print(sqrt(8**2 + 6**2))

    		>>>print(sqrt(-8**2 + 6**2))
    		Traceback (most recent call last)

    		>>>print(m**2 + 3**2)
    		ValueError

    		AssertionError


    '''
    print('Введіть перший катет: ')
    while 1:
        try:
            a = float(input()) #Вводиться значення a,яке є по типу данних float
            break
        except ValueError:
            print('Ви помилились.Спробуйте, будь-ласка, ще раз!')
    print('Введіть другий катет: ')
    while 1:
        try:
            b = float(input()) #Вводиться значення b,яке є по типу данних float
            break
        except ValueError:
            print('Ви помилились.Спробуйте, будь-ласка, ще раз!')
    c = sqrt(a**2 + b**2) #Операція розраховує корінь квадратний з суми квадратів катетів(довжину гіпотенузи)
    P = (a + b + c) #Операція розраховує суму довжин усіх сторін(периметр трикутника)
    S = (a * b)/2  #Розрахування півдобутку катетів(площі трикутника)
    print('Гіпотенуза = ')
    print('%.10f' % c)#Вивід округленого до десяти знаків після коми,числа с,що є гіпотенузою трикутника і по типу данних float
    print('Периметр = ')
    print('%.10f' % P)#Вивід округленого до десяти знаків після коми,числа ,що є периметром трикутника і по типу данних float
    print('Площа = ')
    print('%.10f' % S)#Вивід округленого до десяти знаків після коми,числа ,що є площею трикутника і по типу данних float
    menu()

def second_task():
    ''' Ця функція дізнається чи існує трикутник і чи є він прямокутним
        Args:
    	    a:  float.number
    		b:  float.number
    	Returns:
    	    A float number is the result
    	Exceptions:
    	    >>>print(180-(30+60))

    		>>>print(180-(190+3))
    		Traceback (most recent call last)

    		>>>print(180-(a+2)
    		ValueError

    		AssertionError


    '''
    print('Введіть перши1 кут: ')
    while 1:
        try:
            a = float(input())#Введення значення кута а,по типу данних float
            break
        except ValueError:
            print('Ви помилились.Спробуйте, будь-ласка, ще раз!')
    print('Введіть другий кут: ')
    while 1:
        try:
            b = float(input())#Введення значення кута b,по типу данних float
            break
        except ValueError:
            print('Ви помилились.Спробуйте, будь-ласка, ще раз!')
    c = 180 - (a + b)#Знаходження кута с,віднімаючи від 180 суму двох інших кутів
    if a + b > 180:#Умова існування трикутника,якщо сума двох кутів більше 180 градусів,то трикутник не існує
        print('Трикутник не може існувати')
    elif a + b > c or a + c > b or b + c > a and a > 0 and b > 0 and c > 0:#Друга умова існування трикутника
        print('Трикутник може існувати')
        if a == 90 or b == 90 or c == 90:#Перевірка кутів трикутника на наявність прямого
            print('Трикутник прямокутний')
        else:#Якщо не знайшлося прямого кута,то виконується дана функція
            print('Трикутник не прямокутний')
    menu()

def third_task():
    ''' Ця функція знаходить F(x)
        Args:
    	    x:  float.number

    	Returns:
    	    A int number is the result
    	Exceptions:
    	    >>>print(x=-2)

    	    >>>print(x=m)
    		ValueError

    		AssertionError


    '''
    print('Введіть значення x:')
    while 1:
        try:
            x = float(input())#Введення значення х,який по типу данних є float
            break
        except ValueError:
            print('Ви помилились.Спробуйте, будь-ласка, ще раз!')
    if x <= -3:#Коли х буде меньше або дорівнювати -3,виконується дана функція
        print('F(x)= 9')
    else:
        print('F(x)= ' + str(1/(x**2 + 1)))#Коли х буде більше -3,буде виконуватися функція else
    menu()


def menu():
    print('')
    print('Виберіть пункт меню')
    print('1.Завдання №1')
    print('2.Завдання №2')
    print('3.Завдання №3')
    print('4.Вихід')
    while 1:
        try:
            a = float(input())
            break
        except ValueError:
            print('Ви помилились.Спробуйте, будь-ласка, ще раз!')
    if a == 1:
        first_task()
    if a == 2:
        second_task()
    if a == 3:
        third_task()
    if a == 4:
        exit()
    else:
        print('Спробуйте ще раз')
    menu()

menu()