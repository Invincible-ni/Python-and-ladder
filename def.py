#AdkiNishanth-2020
from random import randint
def gam(pos):
	def Pythons(pos):
	#Ladders throughout the board
		if pos==4:
			pos+=21
		elif pos==13:
			pos+=33
		elif pos==33:
			pos+=16
		elif pos==42:
			pos+=21
		elif pos==50:
			pos+=19
		elif pos==62:
			pos+=19
		elif pos==74:
			pos+=18
	#Snakes throughout the board
		elif pos==27:
			pos-=22
		elif pos==40:
		    pos-=37
		elif pos==43:
		    pos-=25
		elif pos==54:
		    pos-=23
		elif pos==66:
		    pos-=21
		elif pos==76:
		    pos-=18
		elif pos==89:
		    pos-=36
		elif pos==99:
		    pos-=58
	   
		return pos
	k=Pythons(pos)
	return k
	
while True:
	inp=input("throw dice???:")
	if inp=="y":
		pos=1
		m=randint(1,6)
		print(m)
		pos=pos+m
		print("you are at:"+str(gam(pos)))
