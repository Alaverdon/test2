num_tickets = int(input("Введите количество билетов: "))
ages = []
for i in range(num_tickets):
    age = int(input("Введите возраст посетителя: "))
    ages.append(age)
total_price = 0
discount = 0
for age in ages:
    if age < 18:
        total_price += 0
    elif age < 25:
        total_price += 990
    else:
        total_price += 1390
if num_tickets > 3:
    discount = 0.1 * total_price
total_price -= discount
print("Сумма к оплате:", total_price)
