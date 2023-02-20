
from datetime import date
today=date.today()

men1day=int(input("Введите дату рождения первого человека: "))
men1month=int(input("Введите месяц рождения: "))
men1year=int(input("Введите год рождения: "))

age1=today.year-men1year-((today.month,today.day)<(men1month,men1day))

men2day=int(input("Введите дату рождения второго человека: "))
men2month=int(input("Введите месяц рождения: "))
men2year=int(input('Введите год рождения: '))

age2=today.year-men2year-((today.month,today.day)<(men2month,men2day))

if age1>age2:
    print(f"Первый человек старше, ему {age1}")
else:
    print(f"Второй человек старше, ему {age2}")


