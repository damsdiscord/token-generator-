import random
import string
import pathlib
import requests, os, threading, sys, time, random, ctypes, webbrowser,re, hashlib, datetime, os.path
import colorama
from colorama import Fore, init, Back, Style
from datetime import date

os.system("title [dams] Made by dams#1000")

def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write('\r' + Fore.YELLOW +'Starting DamsGen...'+i)
		sys.stdout.flush()
		time.sleep(0.2)

Spinner()

banner = (Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]\n"+ 
Fore.WHITE +Fore.RED +'''\n  
dams' \n\n'''+ Fore.RESET + Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]\n")

os.system("cls")
count = 0
current_path = os.path.dirname(os.path.realpath(__file__))
	
print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
print(Fore.WHITE +Fore.RED +"                                         Welcome to "+Fore.WHITE+" Dams-Gen "+Fore.WHITE+"- 2022 -")
print(Fore.WHITE +Fore.RED +"                                         [1] "+Fore.WHITE+"Token Generator(super fast!)")
print(Fore.WHITE +Fore.RED +"                                         [2] "+Fore.WHITE+"Token Checker(Checks all tokens you generated)")
print(Fore.WHITE +Fore.RED +"                                         [3] "+Fore.WHITE+"Credits")
print(Fore.WHITE +Fore.RED +"                                         [4] "+Fore.WHITE+"Exit")
print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
opcion = input("\nChoice: ")
if opcion=='1':
	os.system("cls")
	print(banner)
	cantidad = input("\nAmount to generate: ")
	while int(count)<int(cantidad):
		Generated = "MT"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
		f= open(current_path +"/"+str("Generated")+str("")+".txt","a")
		f.write(Generated+"\n")
		print(Fore.GREEN +"Token: "+ Fore.RESET + Generated)
		count+=1
		if int(count)==int(cantidad):
			print("\n" + Fore.CYAN +Fore.RED +"Tokens generated successfully!")
			print(Fore.WHITE +Fore.RED +"Tokens saved in Generated.txt")
			input(Fore.RED +Fore.RED +"\nPress enter to exit")
			os.system("cls")
			print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
			print(Fore.RED +Fore.RED +"                                                   Closing!")
			print(Fore.GREEN +Fore.RED +"                                               Have a good day :D")
			print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
			time.sleep(2)
			sys.exit()
			pass
	pass
if opcion=='2':
	os.system("cls")
	print("\n" + banner + "\n")
	with open('Generated.txt', 'r') as f:
	    for line in f:
	        time.sleep(0)
	        token = line.rstrip("\n")
	        headers = {
	            'Authorization': f'{token}'  
	        }
	        src = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)

	        try:
	            if src.status_code == 200:
	                print(f'{Fore.RED}InValid token! >{Fore.RESET} ' + token)
	            else:
	                print(f'{Fore.LIGHTGREEN_EX}Valid token >{Fore.RESET} ' + token)
	        except Exception:
	            print(f"{Fore.CYAN}Error, please contact with dams#1000 {Fore.RESET}")
pass
if opcion=='3':
	os.system("cls")
	print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
	print(Fore.WHITE +Fore.RED +"                                         dams#1000"+Fore.WHITE+" Made by "+Fore.RED+"dams#1000")
	print(Fore.WHITE +Fore.RED +"                                         [Discord] "+Fore.RED+"dams#1000")
	print(Fore.WHITE +Fore.RED +"                                         [Server] "+Fore.RED+"https://dsc.gg/lightgen")
	print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
	input(Fore.RED +Fore.RED +"\nEnter to exit")
	os.system("cls")
	print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
	print(Fore.RED +Fore.RED +"                                                   Closing!")
	print(Fore.GREEN +Fore.RED +"                                               Have a good day :D")
	print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
	time.sleep(2)
	sys.exit()
	pass
if opcion=='4':
	os.system("cls")
	print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
	print(Fore.RED +Fore.RED +"                                                   Closing!")
	print(Fore.GREEN +Fore.RED +"                                               Have a good day :D")
	print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
	time.sleep(2)
	sys.exit()
	pass


