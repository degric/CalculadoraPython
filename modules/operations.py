
# ec = ecuaciones, P..S..T, = 1,2,3 Grado, G =Grado

# Ecuaciones Forma 'ax +b = c'
def ecPG(a, b, c):
    p1 = '{}x + {} = {}'.format(a,b,c)
    p1R = (c - b)
    p2 = '{}x = {}'.format(a, p1R)
    p2R = p1R/a
    p3 = 'x = {}'.format(p2R)
    x = ((c-b)/a)
    resultados = [p1,p2,p3,x]
    return resultados
    
# Ecuaciones Formna 'ax^2 + bx +c  =0'

def ecSG(a,b,c):
    from math import sqrt
    x1 = ((-b)+(sqrt((b**2)-(4*a*c))))/(2*a)
    x2 = ((-b)-(sqrt((b**2)-(4*a*c))))/(2*a)
    resultados = [x1,x2]
    return resultados
