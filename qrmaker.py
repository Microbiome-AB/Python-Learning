import qrcode
img = qrcode.make('Binod Rayamajhee')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")

#Wifi link
wifi_type = "WPA"
wifi_ssid = "iambrp_fpkhr"
wifi_password = "Passw0rd@1234"
wifi = f"WIFI:T:{wifi_type};S:{wifi_ssid};P:{wifi_password};;"
img = qrcode.make(wifi)
type(img)  # qrcode.image.pil.PilImage
img.save("wifi.png")

#SMS send 
phone="1122222"
message="Hello dear"
sms=""

SMSTO:<phone_number>:<message>



#Create QR code generator that send email to users
#Title: My first email using python
#Body: Hello my body...



#Create software that convert English date to Nepali Date

