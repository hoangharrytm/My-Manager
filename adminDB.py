import gspread

from oauth2client.service_account import ServiceAccountCredentials

scopes = [
	'https://www.googleapis.com/auth/spreadsheets',
	'https://www.googleapis.com/auth/drive',
	'https://www.googleapis.com/auth/drive.file',
	'https://spreadsheets.google.com/feeds'
]

creds = ServiceAccountCredentials.from_json_keyfile_name("secretkey.json", scopes)

client = gspread.authorize(creds)
spreadsheet = client.open("My Manager unofficial")

#check admin secret
def listen_secret(admin_username, admin_password):
    worksheet = spreadsheet.sheet1
    admins = worksheet.col_values(4)
    del admins[0]
    for admin in admins:
        admin = admin.split("~>")
        if admin_username == admin[0] and admin_password == admin[1]:
            return True
            break
        else:
            print("You are not admin! Consider using 'main.exe', thank you for spending your time on the product!")
            
def add_homework(deadline, name, description):
    worksheet = spreadsheet.worksheet('Add homework')
    num_of_hw = int(worksheet.acell('D2').value)
    worksheet.update_cell(num_of_hw+2, 1, name) #name of hw
    worksheet.update_cell(num_of_hw+2, 2, description) #description
    worksheet.update_cell(num_of_hw+2, 3, deadline) #deadline
    worksheet.update_acell('D2', num_of_hw+1)

def add_notification():
    pass
    
def view_homework():
    pass
    
def delete_homework():
    pass
    
"""
#alternate
worksheet = spreadsheet.sheet1
num_of_user = int(worksheet.acell('C2').value)
get_user_value = worksheet.col_values(1)
del get_user_value[0]

read_file = open("data.txt", "r")
data = read_file.readline().strip('\n').split(" ")
read_file.close()

# print(data)

# for i in range(0,num_of_user):
# 	if data[0] == get_user_value[i]:
# 		print("yes!")
# 		break
# 	elif i == num_of_user-1:
# 		print(i)
# 		print("no")

result = open("data.txt", "w")
for check_user in range(0, num_of_user):
	if data[0] == get_user_value[check_user]:
		result.write("Username already exist!")
		break
	elif check_user == (num_of_user-1):
		result.write("Success!")
		worksheet.update_cell(num_of_user+2, 1, data[0])
		worksheet.update_cell(num_of_user+2, 2, data[1])
		worksheet.update_acell('C2', num_of_user+1)
result.close()
"""