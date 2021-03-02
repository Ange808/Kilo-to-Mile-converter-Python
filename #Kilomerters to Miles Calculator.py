#Kilomerters to Miles Calculator

KILO = int (input ("Type in KILOMETERS to be converted into MILES\n"))
MILE = int (KILO * 1.6)


if KILO < 0:
    print ("This is a negative number SORRY")
else:
    print (KILO, "Kilometers is", MILE, "Miles")
