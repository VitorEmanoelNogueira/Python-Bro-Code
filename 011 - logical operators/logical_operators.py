# or operator
temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

# and and not operators

temp2 = 0
is_sunny = False

if temp2 >= 28 and is_sunny:
    print("It is HOT outside 🥵")
    print("It is SUNNY ☀")
elif temp2 <= 0 and is_sunny:
    print("It is COLD outside 🥶")
    print("It is SUNNY ☀")
elif 28 > temp2 > 0 and is_sunny:
    print("It is WARM outside 😊")
    print("It is SUNNY ☀")
elif temp2 >= 28 and not is_sunny:
    print("It is HOT outside 🥵")
    print("It is CLOUDY ☁")
elif temp2 <= 0 and not is_sunny:
    print("It is COLD outside 🥶")
    print("It is CLOUDY ☁")
elif 28 > temp2 > 0 and not is_sunny:
    print("It is WARM outside 😊")
    print("It is CLOUDY ☁")