#Host-Maker
#Author iFanpS

import os, sys

print("[ $ ] iFanpS Host-Maker")
ip = input("[ ? ] Put ur GTPS IP:")
os.system('cls')
asu=False
try:
	with open('host.txt', 'r') as konz:
		if f"{ip} growtopia1.com" in konz.read():
			print(f'[ = ] {ip} Already added before!')
		else:
			asu=True;
		konz.close()
	if asu:
		with open('host.txt', 'a') as konz:
			konz.write(f'{ip} growtopia1.com\n{ip} growtopia2.com')
			print('[ + ] File is created')
except:
	print("[ ? ] Something error")
input("[ ! ] Go away/Click anykey to close the door...")
