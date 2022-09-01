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
spreadsheet = client.open("My Manager")
worksheet = spreadsheet.sheet1
num_of_user = int(worksheet.acell('C2').value)
get_user_value = [worksheet.col_values(1),worksheet.col_values(2)]

del(get_user_value[0][0], get_user_value[1][0])

data = []

'''
read_file = open("data.txt", "r")
data = read_file.readline().strip('\n').split(" ")
read_file.close()

print(data)

for i in range(0,num_of_user):
	if data[0] == get_user_value[0][i] and data[1] == get_user_value[1][i]:
		print("yes!")
		break
	elif i == num_of_user-1:
		print(i)
		print("no")
'''

#result = open("data.txt", "w")
def check_data():
    for check_user in range(0, num_of_user):
        if data[0] == get_user_value[0][check_user] and data[1] == get_user_value[1][check_user]:
            return True
            break
        elif check_user == num_of_user-1:
            return False
#result.close()

