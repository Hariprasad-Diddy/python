# Importing phone numner library
import phonenumbers
from phonenumbers import geocoder,timezone,carrier

mobile_no = input("Enter Mobile number with country code : ")

def phone(mobile_no):
    mobile_no = phonenumbers.parse(mobile_no)

    # validating a phone number
    if phonenumbers.is_valid_number(mobile_no):
        print(f"{mobile_no} is a valid Mobile number.")
        
        # get timezone a phone number
        print(timezone.time_zones_for_number(mobile_no))

        # getcarrier of a phone number
        print(carrier.name_for_number(mobile_no,'en'))

        # get region information
        print(geocoder.description_for_number(mobile_no,'en'))
    else:
        print(f"{mobile_no} is not a valid Mobile number.")

    
# caling the function
phone(mobile_no)
