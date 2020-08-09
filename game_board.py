#AdkiNishanth-2020
def Pyladder():
	for i in range(1,11):
		print("--------------------------------------------------")
		for j in range(1,10):
				if i%2!=0:
					count=i*10-10+1
					for l in range(0,10):
						print(count,end=" | ")
						count+=1
					
					break
				if i%2==0:
					ct1=i*10
					for k in range(10,0,-1):
						print(ct1,end=" | ")
						ct1-=1
	
					break
		print()
    
    
Pyladder()    
    
    
