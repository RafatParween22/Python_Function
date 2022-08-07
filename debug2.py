def greet(*names):
    for name in names:
        print("Welcome", name)
greet("Rinki", "Vishal", "Kartik", "Bijender")

a="rafat"
print(a[::-1])

list=[1,]

def num(numbers):
    n=int(input("enter the num"))
    i=1
    while i<len(numbers):
        if numbers[i]%2==0:
            print("even",numbers[i])
        else:
            print("odd",numbers[i])
        i=i+1
num(numbers=[1,2,4,5,6,7,8,9,10])





