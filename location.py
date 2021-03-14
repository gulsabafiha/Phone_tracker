import phonenumbers
from test import number,num

from phonenumbers import geocoder
ch=phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch,"en"))

from phonenumbers import carrier

cb=phonenumbers.parse(num,"RO")
print(carrier.name_for_number(cb,"bn"))