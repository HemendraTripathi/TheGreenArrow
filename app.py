#Shree Ganesh#

import os,sqlite3,requests,json,sys,datetime
from xlsxwriter.workbook import Workbook
from ver import verify_input
from time import sleep
from get_user import get_user
from get_message import get_message
from send_message import send_message
from save_to_excel import save_to_excel


flag, TOKEN, API_TOKEN = verify_input(sys.argv)
if not flag:
	sys.exit(3)
current_month_text = datetime.datetime.now().strftime('%B')
current_year_text = datetime.datetime.now().strftime('%Y')
sheet_name = current_month_text +"_"+current_year_text+".xlsx"

cwd = os.getcwd()
path = os.path.join(cwd,'delivery_data')
print(path)
try:
	os.mkdir(path)
	print(path)
except FileExistsError:
	pass
sheet_name = os.path.join(path,sheet_name)
print(sheet_name)
while True:
	get_user(TOKEN)
	get_message(TOKEN,API_TOKEN)
	send_message(TOKEN)
	save_to_excel(sheet_name)
	if sys.platform == 'win32':
		os.system('cls')
	elif sys.platform == 'linux':
		os.system('')
	print("Sleeping For 30 Seconds.")
	print("""
	
Refreshing ............

      )  (
     (   ) )
      ) ( (
    _______)_
 .-'---------|  
( C|/\/\/\/\/|
 '-./\/\/\/\/|
   '_________'
    '-------'

	""")
	sleep(30)
	
	
	
	
	
