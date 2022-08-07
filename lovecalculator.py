print("welcome to my love calculator game this is very interesting and enjoyful:-")
x=input("enter the name : ")
y=input("enter the name : ")
z=x+y
n=z.lower()
t=n.count("t")
r=n.count("r")
u=n.count("u")
e=n.count("e")
true=t+r+u+e
l=z.count("l")
o=z.count("o")
v=z.count("v")
e=z.count("e")
love=l+o+v+e
love_score=str(true)+str(love)
print(love_score)
# love_score=int(str(true)+str(love))
# if (love_score <10) or (love_score>90):
#     print(f"your love score is{love_score} ,is very wellyou are go together:-- ")
# elif love_score>=40 and love_score<=50:
#     print(f"your love score is{love_score} alright:--")
# else:
#     print("your love{love_score} is")