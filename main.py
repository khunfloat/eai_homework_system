import gspread
import os 
import time
from parinya import LINE
from time import date, time
from dateutil.relativedelta import relativedelta
from oauth2client.service_account import ServiceAccountCredentials
import time

# sheet name
sheet_name = "HOMEWORK E-AI"
# alarm time
alarm_time = "17:00"
# line notify token
Line_Token = '{ Add token here }'

def main():

    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/spreadsheets",
             "https://www.googleapis.com/auth/drive.file",
             "https://www.googleapis.com/auth/drive"]
             
    creds = ServiceAccountCredentials.from_json_keyfile_name(' { Add .json file here }', scope)
    client = gspread.authorize(creds)
    line = LINE(Line_Token)
    sheet = client.open(sheet_name).sheet1 # Open the spreadhseet
    data = sheet.get_all_records()  # Get a list of all records

    def deadlinealarm():

        today = date.today()
        dl= today + relativedelta(days = 1)
        deadline = str(str(int(dl.strftime("%d"))) + "/" + str(int(dl.strftime("%m"))) + "/" + str(int(dl.strftime("%Y"))))            
        return deadline

    def deadlinealarmsat():

        today = date.today()
        dl= today + relativedelta(days = 2)
        deadline = str(str(int(dl.strftime("%d"))) + "/" + str(int(dl.strftime("%m"))) + "/" + str(int(dl.strftime("%Y"))))            
        return deadline

    for row  in data:

        if str(row["DEADLINE"]) == str(deadlinealarm()):
            line.sendtext(os.linesep + "การบ้านที่ต้องส่งวันพรุ่งนี้" + 
                          os.linesep + "SUBJECT : " + str(row["SUBJECT"]) + 
                          os.linesep + "ASSIGNMENT : " + str(row["ASSIGNMENT"]) + 
                          os.linesep + "DETAIL : " + str(row["DETAIL"]) + 
                          os.linesep + "SUBMIT : " + str(row["SUBMIT"]))
        
        elif time.time.now().strftime("%w") == 6 :

            if str(row["DEADLINE"]) == str(deadlinealarmsat()):
                line.sendtext(os.linesep + "การบ้านที่ต้องส่งวันจันทร์" + 
                              os.linesep + "SUBJECT : " + str(row["SUBJECT"]) + 
                              os.linesep + "ASSIGNMENT : " + str(row["ASSIGNMENT"]) + 
                              os.linesep + "DETAIL : " + str(row["DETAIL"]) + 
                              os.linesep + "SUBMIT : " + str(row["SUBMIT"]))


#while(True):

    #date_time = time.time.now()
    #if ((str(date_time.strftime("%X")))[0:5]) == alarm_time :
        #main()
        #time.sleep(61000)
