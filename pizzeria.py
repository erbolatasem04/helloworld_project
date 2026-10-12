item1_name  = "Маргарита"
item1_price = 2200
item1_qty   = 2

item2_name  = "Пепперони"
item2_price = 2700
item2_qty   = 1

item3_name  = "Кола 1л"
item3_price = 700
item3_qty   = 3

item4_name  = "Чизкейк"
item4_price = 1500
item4_qty   = 2

delivery         = True
delivery_price   = 800
discount_percent = 10


print("========= ЧЕК =========")
item1 = item1_price * item1_qty
item2 = item2_price * item2_qty
item3 = item3_price * item3_qty
item4 = item4_price * item4_qty
print(f"{item1_name} {item1_qty} * {item1_price} = {item1}")
print(f"{item2_name} {item2_qty} * {item2_price} = {item2}")
print(f"{item3_name} {item3_qty}* {item3_price} = {item3}")
print(f"{item4_name} {item4_qty}* {item4_price} = {item4}")

all = "Подытог"
all = item1 + item2 + item3 + item4
print("-------------------------")
print("Подытог:           ", all)

discount_percent = 10
sale = all * discount_percent / 100
print("Скидка (10%)       ", sale)

with_sale = all - sale
print("Итог со скидкой:   ", with_sale)

delivery = delivery_price * int(delivery)
print("Доставка:          ", delivery)

print("--------------------------")
amount_to_pay = with_sale + delivery
print("К ОПЛАТЕ:          ", amount_to_pay)
print("==========================")

print('Позиции: 4')
median = all / 4
print('Средняя стоимость позиции:', median)