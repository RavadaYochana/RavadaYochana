'''import phonenumbers as ph
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

number = "+918790479338"
number = ph.parse(number)
print(timezone.time_zones_for_number(number))
print(carrier.name_for_number(number, "en"))
print(geocoder.description_for_number(number, "en"))'''
'''import getpass
database = {"aman.kharwal": "123456", "kharwal.aman": "654321"}
username = input("Enter Your Username : ")
password = getpass.getpass("Enter Your Password : ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter Your Password Again : ")
        break
print("Verified")'''
from countryinfo import CountryInfo
country = CountryInfo("India")
print(country.alt_spellings())
print(country.capital())
print(country.currencies())
print(country.languages())
print(country.borders())
data = country.info()
for i, j in data.items():
  print(f"{i}:>>{j}")
