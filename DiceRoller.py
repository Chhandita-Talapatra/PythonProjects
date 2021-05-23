import random
r=input("Type 'roll' for rolling the dice : ")
if r=='roll' :
    output=random.randint(1,6)
    if output==1 :
        print("|*|")
    elif output==2:
        print("|**|")
    elif output==3 :
        print("|***|")
    elif output==4 :
        print("|* *|")
        print("|* *|")
    elif output==5:
        print("|* *|")
        print("| * |")
        print("|* *|")
    elif output==6 :
        print("|* * *|")
        print("|* * *|")
        print("It's perfect six !!")
else :
    print("Type properly")