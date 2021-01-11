#Host-Maker
#Author iFanpS
import os, sys

print("[ $ ] iFanpS Host-Maker")
ip = input("[ ? ] Put ur GTPS IP:")
os.system('cls')
asu=False
kontol=True
try:
	if kontol:
		with open('host.txt', 'a') as konz:
			konz.write(f'{ip} growtopia1.com\n{ip} growtopia2.com')
			print(f'[ = ] {ip} File is created')
	else:
			asu=True;
			konz.close()
	if asu:
		with open('host.txt', 'r') as konz:
			if f'{ip} growtopia1.com' in file.read():
				print(f'ip already in file')
except:
	print("[ ? ] Something error")
input("[ ! ] Go away/Click anykey to close the door...")
