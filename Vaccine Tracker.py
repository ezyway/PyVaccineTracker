"""

    Checking availability of the vaccines

"""

import ctypes
import os
import requests as req
import webbrowser as browser
import time
import datetime as dt
import winsound
import configparser as cp
import msvcrt as m

class VaccineTracker:
    def __init__(self):
        os.system('cls')

        self.fileLoc = os.path.dirname(__file__) + "\\"   # Get File Location
        flag = None
        configFile = "Preferences.ini"


        # Use Old Details
        if os.path.exists(self.fileLoc + configFile):   # Check for save file
            self.saveFile = self.fileLoc + configFile
            flag = input("Previous Preferences Found, Use that? [y/n]: ")
        else:
            print("No Preferences Were Found")


        # Display Preference Setting
        print("Select Display Preferences")
        print("\n1. Full")
        print("2. Compact")
        self.displayPref = input("\n Choose (1 or 2): ")


        # Use .ini or start over
        if flag == "y" or flag == "Y":
            os.system('cls')
            print("Using Old Settings")

            # Reads from the .ini File
            configRead = cp.ConfigParser()
            configRead.read(self.fileLoc + configFile)
            section = configRead.sections()[0]      # Gets the first section
            
            # Gets Today and Tomorrow
            date = dt.date.today().strftime("%d-%m-%Y")
            dateTom = str(int(date[:-8])+1)+date[2:]

            # Select Dates
            print("\n1. " + date + " (Today)")
            print("2. " + dateTom + " (Tomorrow)")
            dateSel = input("\nChoose Date (1 or 2): ")

            if section == "Pincode":
                print("Using Pincode: " + configRead.get(section,"code"))
                print("\n** Press any key to start **")
                m.getch()
                while True:
                    if dateSel == "1":
                        self.get_slot_pincode(configRead.get(section,"code"),date)
                    else:
                        self.get_slot_pincode(configRead.get(section,"code"),dateTom)
                    time.sleep(5)
            
            elif section == "District":
                print("Using District: " + configRead.get(section,"name"))
                print("\n** Press any key to start **")
                m.getch()
                while True:
                    if dateSel == "1":
                        self.get_slot_district(configRead.get(section,"name"),date)
                    else:
                        self.get_slot_district(configRead.get(section,"name"),dateTom)
                    time.sleep(5)


        elif flag == "n" or flag == "N" or flag == None:
            os.system('cls')
            print("Using new Settings")

            print("\nCOVID Vaccination Slot Notifier Bot v-Alpha2\n")

            print("1. Get Slot By Pin")
            print("2. Get Slot By District\n")
            
            choice = int(input("Input a Number: "))

            os.system('cls')

            # Gets config parser obj and file obj to write the config
            configWrite = cp.ConfigParser()
            file = open(self.fileLoc + configFile,"w")


            if choice == 1:
                pincode = input("Enter the pincode: ")
                date = input("Enter Date in DD-MM-YYYY format: ")

                # Add Section; set code = value; write to file; close file
                configWrite.add_section("Pincode")
                configWrite.set("Pincode","code",str(pincode))
                configWrite.write(file)
                file.close()

                while True:
                    self.get_slot_pincode(pincode,date)
                    time.sleep(5)
            
            elif choice == 2:
                district = input("Enter District Name: ")
                date = input("Enter Date in DD-MM-YYYY format: ")
                
                # Add Section; set code = value; write to file; close file
                configWrite.add_section("District")
                configWrite.set("District","name",district)
                configWrite.write(file)
                file.close()

                while True:
                    self.get_slot_district(district,date)
                    time.sleep(5)

            

        else:
            print("Invalid Selection. Exiting ...")
            exit()

        


        




# end Init -----------------------------------------------------------------------------------------------------------------

    def get_URL(self, urlType):
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



# end get_URL -----------------------------------------------------------------------------------------------------------------

    def get_slot_pincode(self, pin, date):
        os.system('cls')

        # https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=110001&date=31-03-2021
        # Requests to Cowin API
        res = req.get(self.get_URL("pincode"), params = { "pincode":pin, "date":date })
        self.display(res)



# end get_slot_pincode -----------------------------------------------------------------------------------------------------------------

    def get_slot_district(self, districtName, date):
        os.system('cls')

        districts_json = {"districts": [{"district_id": 154, "district_name": "Ahmedabad"}, {"district_id": 770, "district_name": "Ahmedabad Corporation"}, {"district_id": 174, "district_name": "Amreli"}, {"district_id": 179, "district_name": "Anand"}, {"district_id": 158, "district_name": "Aravalli"}, {"district_id": 159, "district_name": "Banaskantha"}, {"district_id": 180, "district_name": "Bharuch"}, {"district_id": 175, "district_name": "Bhavnagar"}, {"district_id": 771, "district_name": "Bhavnagar Corporation"}, {"district_id": 176, "district_name": "Botad"}, {"district_id": 181, "district_name": "Chhotaudepur"}, {"district_id": 182, "district_name": "Dahod"}, {"district_id": 163, "district_name": "Dang"}, {"district_id": 168, "district_name": "Devbhumi Dwaraka"}, {"district_id": 153, "district_name": "Gandhinagar"}, {"district_id": 772, "district_name": "Gandhinagar Corporation"}, {"district_id": 177, "district_name": "Gir Somnath"}, {"district_id": 169, "district_name": "Jamnagar"}, {"district_id": 773, "district_name": "Jamnagar Corporation"}, {"district_id": 178, "district_name": "Junagadh"}, {"district_id": 774, "district_name": "Junagadh Corporation"}, {"district_id": 156, "district_name": "Kheda"}, {"district_id": 170, "district_name": "Kutch"}, {"district_id": 183, "district_name": "Mahisagar"}, {"district_id": 160, "district_name": "Mehsana"}, {"district_id": 171, "district_name": "Morbi"}, {"district_id": 184, "district_name": "Narmada"}, {"district_id": 164, "district_name": "Navsari"}, {"district_id": 185, "district_name": "Panchmahal"}, {"district_id": 161, "district_name": "Patan"}, {"district_id": 172, "district_name": "Porbandar"}, {"district_id": 173, "district_name": "Rajkot"}, {"district_id": 775, "district_name": "Rajkot Corporation"}, {"district_id": 162, "district_name": "Sabarkantha"}, {"district_id": 165, "district_name": "Surat"}, {"district_id": 776, "district_name": "Surat Corporation"}, {"district_id": 157, "district_name": "Surendranagar"}, {"district_id": 166, "district_name": "Tapi"}, {"district_id": 155, "district_name": "Vadodara"}, {"district_id": 777, "district_name": "Vadodara Corporation"}, {"district_id": 167, "district_name": "Valsad"}]}
        
        
        districtID = None
        
        # Loop through all districts; if entered name is there in JSON; get the id of that district
        for d in districts_json["districts"]:
            if districtName.lower() in d["district_name"].lower():
                districtID = d["district_id"]

        # if no district ID is found, then call the ficntion again
        if districtID == None:
            self.get_slot_district()
            exit()

        # Requests to Cowin API
        res = req.get(self.get_URL("district"), params={"district_id":districtID, "date":date})
        self.display(res)


# end get_slot_district -----------------------------------------------------------------------------------------------------------------   

    def display(self, res):
        if res.status_code == 200:  # For Successfull Data Fetch
            resJSON = res.json()

            # print(resJSON["sessions"])
            data = resJSON["sessions"]
            if data == []:
                print("No Centers was found")
            else:
                for key in data:
                    if self.displayPref == "1":
                        print("Center ID: " + str(key["center_id"]))
                        print("Center Name: " + str(key["name"]))
                        print("Center Address: " + str(key["address"]))
                        print("State: " + str(key["state_name"]))
                        print("District: " + str(key["district_name"]))
                        print("Block: " + str(key["block_name"]))
                        print("Pincode: " + str(key["pincode"]))
                        print("From - To: " + str(key["from"][:-3] + " - " + key["to"][:-3]))
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
                    else:
                        print("Center Name: " + str(key["name"]))
                        print("Center Address: " + str(key["address"]))
                        print("District: " + str(key["district_name"]))
                        print("From - To: " + str(key["from"][:-3] + " - " + key["to"][:-3]))
                        print("Date: " + str(key["date"]))
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
                        if ctypes.windll.user32.MessageBoxW(None, "Open Website to book? [Clicking OK will terminate the program.]", "Wanna Book?", 1) == 1:
                            browser.open("https://selfregistration.cowin.gov.in/")
                            exit()

        elif res.status_code == 500:
            print("Cowin API's Internal Server Error")
        else:
            print("Some Error was there. Error Code: " + str(res.status_code))


# end display -----------------------------------------------------------------------------------------------------------------





vt = VaccineTracker()
