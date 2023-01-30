n=int(input('Введите возраст: '))
#n>=1 and n<=99

if n==1 or n==21 or n==31 or n==41 or n==51 or n==61 or n==71 or n==81 or n==91:
    print("Мне",n,"год")
elif n>=2 and n<=4 or n>=22 and n<=24 or n>=32 and n<=34 or n>=42 and n<=44 or n>=52 and n<=54 or n>=62 and n<=64 or n>=72 and n<=74 or n>=82 and n<=84 or \
        n>=92 and n<=94:
    print("Мне",n,"года")
elif n>=5 and n<=20 or n>=25 and n<=30 or n>=35 and n<=40 or n>=45 and n<=50 or n>=55 and n<=60 or n>=65 and n<=70 or n>=75 and n<=80 or n>=85 and n<=90 or\
        n>=95 and n<=99:
    print("Мне",n,"лет")
else:
    print("Мне",n,"лет","год","года")
