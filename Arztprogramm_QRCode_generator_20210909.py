from datetime import datetime
import pyqrcode #import the following modules pip install pyqrcode, pip install pypng, pip install pillow, pip install pyzbar
from PIL import Image


def generate_qr_code ():
    name_of_med = input("Please enter the name of the medication  ")
    now = datetime.now()
    purchase_date = now.strftime ("%Y-%m-%d") #tried to do with purchase_date = date.today(), but returned in wrong format
    expiry_date = input("Please enter the expiry date of the medication in the format YYYY-MM-DD  ")
    number_of_pills_start = input("Please enter how many pills there are in the container  ")
    dosis_per_day = input("Please indicate the dosis (nr. of pills per day) ")
    place_of_storage = input("Please indicate where the medication has to be stored (enter F for fridge and C for cupboard)  ")
    if place_of_storage.upper() == "C":
        place_of_storage = "cupboard"
    elif place_of_storage.upper() == "F":
        place_of_storage = "fridge"
    else:
        if place_of_storage.upper != "C" and place_of_storage.upper != "F":
            place_of_storage = input("Please indicate correctly where medication has to be stored (enter F for fridge and C for cupboard)  ")

    list_with_meds = []
    list_with_meds.append(name_of_med)
    list_with_meds.append(purchase_date)
    list_with_meds.append(expiry_date) 
    list_with_meds.append(number_of_pills_start)
    list_with_meds.append(dosis_per_day)
    list_with_meds.append(place_of_storage)
    print(list_with_meds)
    return list_with_meds


#generate QR code
qr_code = pyqrcode.create(str(generate_qr_code()))
qr_code.png("myQRcode4.png", scale=8) #if you use the same filename, it will be overwritten, so have to change name to get a new QR code







#checks einbauen ob Eingabe = int





        