import numbers


def sum(numbers):
    sum=0
    i=0
    while i<len(numbers):
        sum=sum+numbers[i]
        i=i+1
    print(sum)
sum([1,2,3,4,5])