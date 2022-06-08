from time import sleep
from os import system, name

grind = False
menupage = False
money = 0
multiple = 1000
listmult = [2, 4, 6, 9, 12, 50, 90, 200, 700, 1000]
listprc = [4000, 5000, 7000, 12000, 30000, 100000, 500000, 900000, 1200000, 5000000]

def tutor():
	print("Type anything to grind money!\nTo leave type 'exit'!")
	sleep(2)

def shop():
	global money, multiple
	many = len(listmult)
	for i in range(many):
		print("[",i,"] Multiple",listmult[i],"x (",listprc[i],")")
	buy = int(input("\nWhat you gonna buy sir?"))
	if buy == 1:
		if money >= listprc[1]:
			multiple = listmult[1]
			money = money - listprc[1]
		else:
			print("You don't have enough money!")
	elif buy == 2:
		if money >= listprc[2]:
			multiple = listmult[2]
			money = money - listprc[2]
		else:
			print("You don't have enough money!")
	elif buy == 3:
		if money >= listprc[3]:
			multiple = listmult[3]
			money = money - listprc[3]
		else:
			print(".")
	elif buy == 4:
		if money >= listprc[4]:
			multiple = listmult[4]
			money = money - listprc[4]
		else:
			print("You don't have enough money!")
	elif buy == 5:
		if money >= listprc[5]:
			multiple = listmult[5]
			money = money - listprc[5]
		else:
			print("You don't have enough money!")
	elif buy == 6:
		if money >= listprc[6]:
			multiple = listmult[6]
			money = money - listprc[6]
		else:
			print("You don't have enough money!")
	elif buy == 7:
		if money >= listprc[7]:
			multiple = listmult[7]
			money = money - listprc[7]
		else:
			print("You don't have enough money!")
	elif buy == 8:
		if money >= listprc[8]:
			multiple = listmult[8]
			money = money - listprc[8]
		else:
			print("You don't have enough money!")
	elif buy == 9:
		if money >= listprc[9]:
			multiple = listmult[9]
			money = money - listprc[9]
		else:
			print("You don't have enough money!")
	elif buy == 10:
		if money >= listprc[10]:
			multiple = listmult[10]
			money = money - listprc[10]
		else:
			print("You don't have enough money!")
	else:
		print("Error!")
names = input("Enter Your Name!")
system("cls")
sleep(2)
print("Welcome to Typing Game!")
sleep(1)
print("Here you can do in this game!")
sleep(1)
menupage = True
while menupage == True:
	print("Your Money:",money,"Multiple:",multiple,"x\n\n")
	print("[1] Start grinding money!")
	print("[2] Upgrade Tools!")
	menu = int(input("\n:"))
	if menu == 1:
		tutor()
		menupage = False
		grind = True
	elif menu == 2:
		shop()
	else:
		print("Sorry we couldn't find",menu,"page")
	while grind == True:
		uss = input("::")
		if uss == 'exit':
			grind = False
			menupage = True
			uss = input("enter anything to continue")
		else:
			duid = len(uss) * multiple
			print("You got",duid)
			money = money + duid

