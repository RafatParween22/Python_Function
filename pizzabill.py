size=int(input("enter the no"))
apprani=int(input("enter the num"))
extra=int(input("enter the num"))
bill=0
if size=="s":
    bill+=15
elif size=="m":
    bill+=20
else:
    bill+=25
if apprani=="y":
    bill+=2
    if apprani=="s":
        bill+=3
    else:
        bill+=4
if extra=="y":
    bill+=1
print(f"all the bills in this{bill} order") 

