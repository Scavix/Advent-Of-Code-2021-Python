with open('input.txt') as f:
    lines = f.readlines()
data=[]
for i in lines:
    data.append(int(i))

# Part 1
counter = 0
for i in range(1,len(data)):
    if data[i]>data[i-1]:
        counter+=1
print(counter)

# Part 2
tmp1 = 0
tmp2 = 0
counter = 0
for i in range(3,len(data)):
    tmp1 = data[i-1] + data[i-2] + data[i-3]
    tmp2 = data[i] + data[i-1] + data[i-2]
    if tmp2 > tmp1:
        counter+=1
print(counter)