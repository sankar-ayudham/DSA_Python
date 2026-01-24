

a=[1,2,3,4]
b=[5,6,7,8]
c=a+b
print(c)


c = a*2
print(c)

#functions
print(sum(a))
print(min(a))
print(max(a))
print(len(a))

total=[]
count=0
while (True):
    inp =input("enter a number")
    if inp =="done": break
    value =float(inp)
    total.append(value)

avarage=sum(total)/len(total)

print("avarage:",avarage)