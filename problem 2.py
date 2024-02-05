import math
def parta():
    ''' this does equation 1 for part b, first by putting the numbers that will be used'''
    x_0=0
    x_1=2
    xtot=1e-4
    maxiter=5
    def funct(x):
        '''this is the euqation to part a to part b'''
        f_x = x- 3*math.cos(x)
        return f_x
    for i in range(1,maxiter, 1):
        '''this does the caculations to get a value for the secant method'''
        f_x_0 = funct(x_0)
        f_x_1 = funct(x_1)
        print(str(i) + 'x:' +str(x_1) + ' - ' + str(f_x_1))
        if abs(f_x_1) < xtot:
            break
        x_2=x_1-f_x_1 * ((x_1-x_0)/(f_x_1 - f_x_0))
        x_0=x_1
        x_1=x_2
    print("\n")
    print(f'zero at x-3cos(x):x=' + str(x_1) + ',f(x)=' + str(f_x_1) )
def partb():
    ''' this does equation 2 for part b, first by putting the numbers that will be used'''
    x_0=0
    x_1=2
    xtot=1e-8
    maxiter=15
    def funct(x):
        '''this is the euqation to part b to part b'''
        f_x = math.cos(2*x) - x**3
        return f_x
    for i in range(1,maxiter, 1):
        '''this does the caculations to get a value for the secant method'''
        f_x_0 = funct(x_0)
        f_x_1 = funct(x_1)
        print(str(i) + 'x:' +str(x_1) + ' - ' + str(f_x_1))
        if abs(f_x_1) < xtot:
            break
        x_2=x_1-f_x_1 * ((x_1-x_0)/(f_x_1 - f_x_0))
        x_0=x_1
        x_1=x_2
    print("\n")
    print(f'zero at cos(2x) -x^3:x=' + str(x_1) + ',f(x)=' + str(f_x_1) )

def partc():
    ''' this does equation 3 for part b, first by putting the numbers that will be used'''
    x_0=0
    x_1=2
    xtot=1e-8
    maxiter=3
    def funct(x):
        '''this is the euqation to part c to part b'''
        f_x = math.cos(2*x)*x**3
        return f_x
    for i in range(1,maxiter, 1):
        '''this does the caculations to get a value for the secant method'''
        f_x_0 = funct(x_0)
        f_x_1 = funct(x_1)
        print(str(i) + 'x:' +str(x_1) + ' - ' + str(f_x_1))
        if abs(f_x_1) < xtot:
            break
        x_2=x_1-f_x_1 * ((x_1-x_0)/(f_x_1 - f_x_0))
        x_0=x_1
        x_1=x_2
    print("\n")
    print(f'zero at cos(2x)*x^3:x=' + str(x_1) + ',f(x)=' + str(f_x_1) )
def main():
    '''this just puts everything into a main function like i was asked to do'''
    parta()

    partb()

    partc()


if __name__ == "__main__":
    '''displays main function'''
    main()

