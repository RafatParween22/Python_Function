# def num(n):
#     i=1
#     while i<=10:
#         b=n*i
#         i=i+1
#         print(b)
# num(n=int(input("enter the num")))

def num(speed):
    b=(speed-70)//5
    if speed<70:
        print("70")
    if(speed-70)//5:
        print(b)
    if b < 12:
        print("(license suspended)") 
num(speed=int(input("enter the num")))



