#Day 3 Part 2
with open("input.txt","r") as sig:
    list1=sig.read().split()

length=len(list1)
g_rate=0

data=list1

while len(data) > 1:
    for i in range(len(data[0])):
        summe=0
        ones=[]
        zeros=[]

        for num in data:
            number=int(num[i])
            summe+=int(number)

            if number==0:
                zeros.append(num)
            else:
                ones.append(num)

        if summe >= len(data)/2:
            data=ones
        else:
            data=zeros

print("key = ",data)
print("ones = ",ones)
print("zeros = ",zeros)