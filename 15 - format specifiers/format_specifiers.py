# {:flags} format a value based on what flags are inserterd
# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ use a plus sign to indicate positive value
# := place sign to leftmost position
# : = insert space before positive numbers
# :, = comma separator

price1 = 23233.12312
price2 = -233987.23
price3 = 1231223.45

print(f"Price 1 is ${price1:.3f}")
print(f"Price 2 is ${price2:20}")
print(f"Price 1 is ${price1:010}")
print(f"Price 1 is ${price1:<10}")
print(f"Price 1 is ${price1:>10}")
print(f"Price 1 is ${price1:^10}")
print(f"Price 3 is ${price3:+10}")
print(f"Price 1 is ${price1: }")
print(f"Price 3 is ${price3:,}")
print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")