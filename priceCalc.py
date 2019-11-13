#программа для расчета цены для интернет-магазина
#расчет по формуле: (закупка + наценка)*1,67
from termcolor import colored

def calc(price, coef):
    price = price + coef
    print(colored("---------------------------------------", 'grey'))
    print(colored('Закупка', 'cyan'), colored("+", 'green'), colored("наценка", 'cyan'),
          colored(coef, 'green'), colored("$", 'red'), colored("=", 'cyan'),
          colored(price, 'green'), colored("$", 'red'))
    price = price * k
    print(colored("---------------------------------------", 'grey'))
    print(colored("Цена без скидки =", 'cyan'),
          colored(float('{:.3f}'.format(price)), 'green', None, ['bold', 'underline']), colored('$', 'red'))

c = "cyan"
g = "green"
rd = "red"
y = "yellow"
u = "underline"
opt = ""
l = ""
k = 1.67
r = 0

while True:

    opt = float(input(colored("Какая, будет, закупочная цена? ", 'yellow')))
    if opt == 0:
        print("End of program")
        break
    if opt < 0:
        print(colored("Цена не может быть отрицательной", rd, None, ['bold', u]), ">>", opt, "<<")
    if 5 > opt >= 1:
        r = 4.5
        calc(opt, r)
    elif 7 > opt >= 5:
        r = 5
        calc(opt, r)
    elif 10 > opt >= 7:
        r = 5.5
        calc(opt, r)
    elif 15 > opt >= 10:
        r = 5.5
        calc(opt, r)
    elif 20 > opt >= 15:
        r = 6
        calc(opt, r)
    elif 30 > opt >= 20:
        r = 6.5
        calc(opt, r)
    elif 40 > opt >= 30:
        r = 7
        calc(opt, r)
    elif 50 > opt >= 40:
        r = 7.5
        calc(opt, r)
    elif 60 > opt >= 50:
        r = 8
        calc(opt, r)
    elif 80 > opt >= 60:
        r = 9
        calc(opt, r)
    elif 100 > opt >= 80:
        r = 10
        calc(opt, r)
    print(colored("++++++++++++++++++++++++++++++++++++++++", 'blue', 'on_grey'))
