number_of_items = int(input("number of items: "))
if number_of_items < 0:
    print("invalid item number!")
    number_of_items = int(input("number of items: "))
total_price = []
for i in range(0, number_of_items):
    price_of_item = float(input("price of item " + str(i+1) + ":"))
    total_price.append(price_of_item)
    if price_of_item < 0:
        print("invalid number")
total_price = sum(total_price)
if total_price > 100:
    discount = total_price /10
    total_price -= discount
print("total price for {0} items is ${1:.2f}".format(number_of_items,total_price))
