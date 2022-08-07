# def num(list,list1):
#     i=0
#     emp=[]
#     while i<len(list):
#         sum=0
#         sum=sum+list[i]+list1[i]
#         emp.append(sum)
#         i=i+1
#     print(emp)
# num([50,60,10],[10,20,13])

def num (list,list1):
    i=0
    while i<len(list):
        sum=0
        sum=sum+list[i]+list1[i]
        i=i+1
        print(sum)
num([50,60,10],[10,20,13])