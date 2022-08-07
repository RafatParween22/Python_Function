def num(numbers_list):
    i=0
    max=0
    while i<len(numbers_list):
        if numbers_list[i]>max:
            max=numbers_list[i]
        i=i+1
    print(max)
num(numbers_list=[1,2,3,4,5,6,7,10,-2])

numbers_list=[1,2,3,4,5,6,7,10,-2]
x=max(numbers_list)
print(x)

