begin = input("What are we converting today? Mass (m), speed (s), or temperature (t)? : ")

if begin.lower().strip() == "m":
    mass = (input("What are you converting to? Pounds (lbs) or Kilograms(kg) "))

    if mass.lower().strip() == "lbs":
        pounds = float(input("Enter mass in pounds: "))
        kilos = (pounds / 2.2046226218)
        print('%0.2f lbs is about: %0.3f kg' % (pounds, kilos))
    if mass.lower().strip() == "kg":
        Kilos = float(input("Enter mass in kilos: "))
        Pounds = (Kilos * 2.2046226218)
        print("%0.3f kg is about: %0.2f kg" % (Kilos, Pounds))

if begin.lower().strip() == "s":
    mass = (input("What are you converting to? Miles/Hour (mph) or Kilometers/Hour (kmh) "))

    if mass.lower().strip() == "mph":
        miles = float(input("Enter speed in Miles/Hour: "))
        kM = (miles * 1.60934)
        print('%0.1f mph is about: %0.1f kmh' % (miles, kM))
    if mass.lower().strip() == "kmh":
        KM = float(input("Enter speed in Kilometers/Hours: "))
        Miles = (KM / 1.60934)
        print('%0.1f kmh is about: %0.1f mph' % (KM, Miles))


if begin.lower().strip() == "t":
    temp = input("What temperature are you converting to? Fahrenheit (f) or Celsius (c) ?:  ")

    if temp.lower().strip() == "c":
        fahrenheit = float(input(" Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print('%.1f Fahrenheit is: %0.1f Celsius' % (fahrenheit, celsius))

    if temp.lower().strip() == "f":
        Celsius = float(input(" Enter temperature in Celsius: "))
        Fahrenheit = (Celsius * 9/5) + 32
        print('%.1f Celsius is: %0.1f Fahrenheit' % (Celsius, Fahrenheit))