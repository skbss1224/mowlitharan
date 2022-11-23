print("-------------------BUSTICKET RESERVATION-----------------")
place=input("enter your place:")
if(place=="chennai"):
    print("you are selected place:",place)
    bustype=input("enter the bus type:")
    if(bustype=="ordinary"):
        print("you are selected",bustype)
        amount=int(input("enter the amount:"))
        if(125<=amount):
            print("you travel in this bus")
            bal=amount-125
            print("your balance amount is",bal)
        else:
            print("insuffiecient amount")
    elif(bustype=="delux"):
        print("you are selected",bustype)
        amount=int(input("enter the amount:"))
        if(150<=amount):
            print("you travel in this bus")
            bal=amount-150
            print("your balance amount is",bal)
        else:
            print("insuffiecient amount")
    elif(bustype=="superdelux"):
        print("you are selected",bustype)
        amount=int(input("enter the amount:"))
        if(175<=amount):
            print("you travel in this bus")
            bal=amount-175
            print("your balance amount is",bal)
        else:
            print("insuffiecient amount")
    elif(bustype=="sleeper"):
        print("you are selected",bustype)
        amount=int(input("enter the amount:"))
        if(200<=amount):
            print("you travel in this bus")
            bal=amount-200
            print("your balance amount is",bal)
        else:
            print("insuffiecient amount")    
    else:
        print("A/C bus service not available")
elif(place=="coimbatore"):
    print("you are selected place:",place)
    bustype=input("enter the bus type:")
    if(bustype=="ordinary"):
        print("you are selected",bustype)
        amount=int(input("enter the amount:"))
        if(100<=amount):
            print("you travel in this bus")
            bal=amount-100
            print("your balance amount is",bal)
        else:
            print("insuffiecient amount")
    elif(bustype=="delux"):
        print("you are selected",bustype)
        amount=int(input("enter the amount:"))
        if(125<=amount):
            print("you travel in this bus")
            bal=amount-125
            print("your balance amount is",bal)
        else:
            print("insuffiecient amount")
    elif(bustype=="superdelux"):
        print("you are selected",bustype)
        amount=int(input("enter the amount:"))
        if(150<=amount):
            print("you travel in this bus")
            bal=amount-150
            print("your balance amount is",bal)
        else:
            print("insuffiecient amount")
    elif(bustype=="sleeper"):
        print("you are selected",bustype)
        amount=int(input("enter the amount:"))
        if(175<=amount):
            print("you travel in this bus")
            bal=amount-175
            print("your balance amount is",bal)
        else:
            print("insuffiecient amount")    
    else:
        print("A/C bus service not available")    
else:
    print("only two places available in this bus chennai and coimbatore")