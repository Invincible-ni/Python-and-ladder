#AdkiNishanth-2020

from random import randint

print("<--------- WELCOME TO PYTHON AND LADDER --------->")







inp=input("Enter your option: 1)Play the GAME / 2)Exit :")


def enterGame():
	name=input("Enter your name :")
	print("\r")
	print(name+", to throw the DICE until you get bored ,ENTER 'y' ... ENTER 'exit' to CLOSE the GAME")
	print("\r")
	print("GAME STARTS.....")
	print("\r")
	Game()
	
def Game():
	n=input("Throw DICE :")
	if n=="exit":
		inp=input("ARE YOU SURE ???(Y/N) :")
		if inp=="Y":
			print("STOPPING PYTHON & LADDERS................")
			exit(0)
		elif inp=="N":
			print("Continue the GAME...")
			Game()

	if n=="y":
			pos=1
			m=randint(1,6)
			print(m)
			pos=pos+m
			print("YOU ARE STANDING AT :"+str(pos))
				
			
				

			
			
			


		
		
	
	

if inp=="2":
	exit(0)
	
if inp=="1":
	enterGame()
	
	

