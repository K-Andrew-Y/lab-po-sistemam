def add (x,y):
    return x+y
def subtruct (x,y):
    return x-y
def multiply (a,b):
    return a*b
def divide (x,y):
    if y==0:
        return "Ошибка. Деление на ноль"
    else:
        return x/y

print(subtruct (10,4))
print(add (3,4))
print(multiply (2,4))
print(divide (10,2))