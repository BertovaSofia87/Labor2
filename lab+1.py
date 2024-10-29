salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
salarys = 0

for i in range(months):
    spend = (spend*increase)+spend
    salarys = salary + salarys
podushka = salarys - spend
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(podushka))

