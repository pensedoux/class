import random
l=["r","p","s"]
k=0
f=0
my= {'s':'Scissors', 'p':'Paper' ,'r':'Rock'}
while True:
	print(my)
	u=input("Choose--->")
	if u=='n':
		print("game over")
		print("Total computer score--->",k)
		print("Total User score-->",f)
		exit()
	c=random.choice(l)
	print("computer chooses",c)
	if u==c:
		print("tie-------",my[u],"----user hav choosen------",my[c],"---computer hav chosen")
		print("computer score",k)
		print("User score",f)
	elif  (l.index(u)+1)%3 == l.index(c)%3:
		f=k+1
		print("computer wins-------",my[u],"----user hav choosen------",my[c],"---computer hav chosen")
		print("computer score",k)
		print("User score",f)
	else:
		f=f+1
		print("user wins-------",my[u],"----user hav choosen------",my[c],"---computer hav chosen")
		print("computer score",k)
		print("User score",f)