num = int(input("Enter the number of visitors - "))
pos = 0
price = 0
print("enter the age of...")
while pos < num:
    pos += 1
    age = int(input("visitor #" + str(pos) + " - "))
    if age >= 25:
        price += 1390
    elif 18 <= age < 25:
        price += 990
if num >= 3:
    price *= 0.9
print(f" - it costs ₽{int(price)}")
