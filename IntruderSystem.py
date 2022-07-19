from boltiot import Bolt, Sms #Import Sms and Bolt class from boltiot library
import json, time, datetime

SID = 'AC564a92746f72a51f7ee6cb98546409ce'
AUTH_TOKEN = '7ff3d60bd4db46940563bd5badc55ca4'
FROM_NUMBER = 'whatsapp:+14155238886'
TO_NUMBER = 'whatsapp:+918135078443'
API_KEY = '2ee5fef3-b92d-4b25-8ed3-8af290d9eeca'
DEVICE_ID = 'BOLT8024537'

startingHour = int(input("Starting Hour(enter in 24 hour format): "))
endingHour = int(input("Ending Hour(enter in 24 hour format): "))

bolt = Bolt(API_KEY, DEVICE_ID)
sms = Sms(SID, AUTH_TOKEN, TO_NUMBER, FROM_NUMBER)

while True:
    current_time = datetime.datetime.now()  # Current Time

    try:
        if startingHour < current_time.hour < endingHour:
            lightValue = int(json.loads(bolt.digitalWrite('3', 'HIGH'))['value'])
            print(f"Light ON/OFF state {lightValue}")  # Lights On if the time is between the given range

            buzzValue = int(json.loads(bolt.digitalRead('4'))['value'])
            print(f"Buzzer ON/OFF state: {buzzValue}")  # Buzzer On if the time is between the given range
            time.sleep(10)
            if buzzValue == 1 and lightValue == 1:
                bolt.digitalWrite('0', 'HIGH')
                print("Making request to Twilio to send a SMS")
                response = sms.send_sms("An Intuder has breached your home ")  # Message to phone if someone enters home at that time
                time.sleep(10)
        else:
            bolt.digitalWrite('3', 'LOW')
            print("System will work from 12am to 6am")  # Print if beyond the given time range
            time.sleep(10)
    except Exception as e:
        print("Error occurred: Below are the details")
        print(e)
    time.sleep(10)
