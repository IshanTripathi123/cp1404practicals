num_items = int(input("Number of items: "))
total_price = 0

for i in range(num_items):
    price = float(input("Price of item: "))
    total_price += price

if total_price > 100:
    discount = total_price * 0.1
    total_price -= discount

print(f"Total price for {num_items} items is ${total_price:.2f}")
