a=int(input('a= '))
b=int(input('b= '))
c=int(input('c= '))

if a+b>c and a+c>b and b+c>a:
    print("Треугольник с заданными сторонами существует")
else:
    print("Треугольник с заданными сторонами не существует")
#if