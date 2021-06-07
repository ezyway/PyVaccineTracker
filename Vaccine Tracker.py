"""

    Check the availability

"""

import ctypes
import os
import requests as req
import webbrowser as browser
import time
import datetime as dt
import winsound


def get_URL(urlType):
    URLs = dict()
    URLs = {
        "pincode":"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin",
        "district":"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict",
        "co-ordinates":"https://cdn-api.co-vin.in/api/v2/appointment/centers/public/findByLatLong",
        "calendarByPin":"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin",
        "calendarByDistrict":"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict",
        "calendarByCenter":"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByCenter",
        "certi":"https://cdn-api.co-vin.in/api/v2/registration/certificate/public/download"
        }
    return URLs[urlType]


def get_slot_pincode(pin, date):
    os.system('cls')

    # https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=110001&date=31-03-2021
    res = req.get(get_URL("pincode"), params = { "pincode":pin, "date":date })
    display(res)



def get_slot_district(districtName, date):
    os.system('cls')

    # states_json = {"states": [{"state_id": 1, "state_name": "Andaman and Nicobar Islands"}, {"state_id": 2, "state_name": "Andhra Pradesh"}, {"state_id": 3, "state_name": "Arunachal Pradesh"}, {"state_id": 4, "state_name": "Assam"}, {"state_id": 5, "state_name": "Bihar"}, {"state_id": 6, "state_name": "Chandigarh"}, {"state_id": 7, "state_name": "Chhattisgarh"}, {"state_id": 8, "state_name": "Dadra and Nagar Haveli"}, {"state_id": 37, "state_name": "Daman and Diu"}, {"state_id": 9, "state_name": "Delhi"}, {"state_id": 10, "state_name": "Goa"}, {"state_id": 11, "state_name": "Gujarat"}, {"state_id": 12, "state_name": "Haryana"}, {"state_id": 13, "state_name": "Himachal Pradesh"}, {"state_id": 14, "state_name": "Jammu and Kashmir"}, {"state_id": 15, "state_name": "Jharkhand"}, {"state_id": 16, "state_name": "Karnataka"}, {"state_id": 17, "state_name": "Kerala"}, {"state_id": 18, "state_name": "Ladakh"}, {"state_id": 19, "state_name": "Lakshadweep"}, {"state_id": 20, "state_name": "Madhya Pradesh"}, {"state_id": 21, "state_name": "Maharashtra"}, {"state_id": 22, "state_name": "Manipur"}, {"state_id": 23, "state_name": "Meghalaya"}, {"state_id": 24, "state_name": "Mizoram"}, {"state_id": 25, "state_name": "Nagaland"}, {"state_id": 26, "state_name": "Odisha"}, {"state_id": 27, "state_name": "Puducherry"}, {"state_id": 28, "state_name": "Punjab"}, {"state_id": 29, "state_name": "Rajasthan"}, {"state_id": 30, "state_name": "Sikkim"}, {"state_id": 31, "state_name": "Tamil Nadu"}, {"state_id": 32, "state_name": "Telangana"}, {"state_id": 33, "state_name": "Tripura"}, {"state_id": 34, "state_name": "Uttar Pradesh"}, {"state_id": 35, "state_name": "Uttarakhand"}, {"state_id": 36, "state_name": "West Bengal"}], "ttl": 24}

    # # stateName = input("Enter State Name: ")
    # stateName = "Gujarat"
    # stateID = None
    
    # for s in states_json["states"]:
    #     if stateName.lower() in s["state_name"].lower():
    #         stateID = s["state_id"]
    #         print("Got State ID")

    # if stateID == None:
    #     get_slot_district()
    #     exit()

    districts_json = {"districts": [{"district_id": 154, "district_name": "Ahmedabad"}, {"district_id": 770, "district_name": "Ahmedabad Corporation"}, {"district_id": 174, "district_name": "Amreli"}, {"district_id": 179, "district_name": "Anand"}, {"district_id": 158, "district_name": "Aravalli"}, {"district_id": 159, "district_name": "Banaskantha"}, {"district_id": 180, "district_name": "Bharuch"}, {"district_id": 175, "district_name": "Bhavnagar"}, {"district_id": 771, "district_name": "Bhavnagar Corporation"}, {"district_id": 176, "district_name": "Botad"}, {"district_id": 181, "district_name": "Chhotaudepur"}, {"district_id": 182, "district_name": "Dahod"}, {"district_id": 163, "district_name": "Dang"}, {"district_id": 168, "district_name": "Devbhumi Dwaraka"}, {"district_id": 153, "district_name": "Gandhinagar"}, {"district_id": 772, "district_name": "Gandhinagar Corporation"}, {"district_id": 177, "district_name": "Gir Somnath"}, {"district_id": 169, "district_name": "Jamnagar"}, {"district_id": 773, "district_name": "Jamnagar Corporation"}, {"district_id": 178, "district_name": "Junagadh"}, {"district_id": 774, "district_name": "Junagadh Corporation"}, {"district_id": 156, "district_name": "Kheda"}, {"district_id": 170, "district_name": "Kutch"}, {"district_id": 183, "district_name": "Mahisagar"}, {"district_id": 160, "district_name": "Mehsana"}, {"district_id": 171, "district_name": "Morbi"}, {"district_id": 184, "district_name": "Narmada"}, {"district_id": 164, "district_name": "Navsari"}, {"district_id": 185, "district_name": "Panchmahal"}, {"district_id": 161, "district_name": "Patan"}, {"district_id": 172, "district_name": "Porbandar"}, {"district_id": 173, "district_name": "Rajkot"}, {"district_id": 775, "district_name": "Rajkot Corporation"}, {"district_id": 162, "district_name": "Sabarkantha"}, {"district_id": 165, "district_name": "Surat"}, {"district_id": 776, "district_name": "Surat Corporation"}, {"district_id": 157, "district_name": "Surendranagar"}, {"district_id": 166, "district_name": "Tapi"}, {"district_id": 155, "district_name": "Vadodara"}, {"district_id": 777, "district_name": "Vadodara Corporation"}, {"district_id": 167, "district_name": "Valsad"}]}
    
    
    districtID = None
    
    for d in districts_json["districts"]:
        if districtName.lower() in d["district_name"].lower():
            districtID = d["district_id"]
            print("Got District ID")

    if districtID == None:
        get_slot_district()
        exit()

    res = req.get(get_URL("district"), params={"district_id":districtID, "date":date})
    display(res)

    

def display(res):
    if res.status_code == 200:  # For Successfull Data Fetch
        resJSON = res.json()

        # print(resJSON["sessions"])
        data = resJSON["sessions"]
        for key in data:
            if key["center_id"] == None:
                print("Nothing was found")
            else:
                print("Center ID: " + str(key["center_id"]))
                print("Center Name: " + str(key["name"]))
                print("Center Address: " + str(key["address"]))
                print("State: " + str(key["state_name"]))
                print("District: " + str(key["district_name"]))
                print("Block: " + str(key["block_name"]))
                print("Pincode: " + str(key["pincode"]))
                print("From - To: " + str(key["from"][:-3] + key["to"][:-3]))
                print("Fee: " + str(key["fee_type"]))
                print("Amount: " + str(key["fee"]))
                print("Date: " + str(key["date"]))
                print("Dose 1s: " + str(key["available_capacity_dose1"]))
                print("Dose 2s: " + str(key["available_capacity_dose2"]))
                print("All Dose: " + str(key["available_capacity"]))
                print("Min Age: " + str(key["min_age_limit"]))
                print("Vaccine: " + str(key["vaccine"]))
                print("Slots: " + str(key["slots"]))
                print("\n")

            # 1 OK
            # 2 Cancel
            # 3 abort 
            # 4 retry 
            # 5 ignore
            # 6 Yes
            # 7 No

            # If More than 1 is free
            if key["available_capacity"] > 0:
                # If Ok is clicked
                winsound.Beep(1000,5000)
                if ctypes.windll.user32.MessageBoxW(None, str(key["available_capacity"]) + " Vaccines were found in "+str(key["name"]), "Date: " + str(key["date"]), 0) == 1:
                    # Open Browser
                    if ctypes.windll.user32.MessageBoxW(None, "Open Website to book?", "Wanna Book?", 1) == 1:
                        browser.open("https://selfregistration.cowin.gov.in/")
                        exit()

    elif res.status_code == 500:
        print("Cowin API's Internal Server Error")
    else:
        print("Some Error was there. Error Code: " + str(res.status_code))


def main():
    os.system('cls')
    print("\nCOVID Vaccination Slot Notifier Bot By-NoobDev v-Alpha\n")

    print("1. Get Slot By Pin")
    print("2. Get Slot By District\n")
    
    choice = int(input("Input a Number: "))

    os.system('cls')

    # date = dt.date.today().strftime("%d-%m-%Y")
    # date = str(int(date[:-8])+1)+date[2:]

    if choice == 1:
        pincode = input("Enter the pincode: ")
        date = input("Enter Date in DD-MM-YYYY format: ")
        while True:
            time.sleep(5)
            get_slot_pincode(pincode,date)
    
    elif choice == 2:
        district = input("Enter District Name: ")
        date = input("Enter Date in DD-MM-YYYY format: ")
        while True:
            time.sleep(5)
            get_slot_district(district,date)




    

main()