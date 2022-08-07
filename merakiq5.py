# def fun(list):
#     x=min(list)
#     print(x)
# fun( list = [8, 6, 4, 8, 4, 50, 2,])

list=[8,6,4,8,4,50,2]
i=0
min=list[0]
while i<len(list):
    if list[i]<min:
        min=list[i]
    i=i+1
print(min)