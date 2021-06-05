import phonenumbers
#from test import number
#print(number)
#import sys
#print(sys.path)

while True:
    number = input("Enter the number with contry code  : ")


    from phonenumbers import geocoder
    ch_number = phonenumbers.parse(number,"CH")
    print(geocoder.description_for_number(ch_number,"en"))

    from phonenumbers import  carrier
    service_name = phonenumbers.parse(number)
    print(carrier.name_for_number(service_name,"en"))

    var = input("type Y for continoue and type n for exit  : ")
    var1 = var.lower()
    if var1 == "y":
        continue
    else:
        break
