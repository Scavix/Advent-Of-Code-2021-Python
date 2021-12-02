with open('input.txt') as f:
    lines = f.readlines()
data=[]
for i in lines:
    #data.append(int(i))
    data.append(i)

# Part 1
hor=0
ver=0
for i in data:
    tmp = i.split(' ')
    if 'up' in tmp:
        ver-=int(tmp[1])
    elif 'down' in tmp:
        ver+=int(tmp[1])
    elif 'forward' in tmp:
        hor+=int(tmp[1])
print(hor*ver)

# Part 2
hor=0
ver=0
aim=0
for i in data:
    tmp = i.split(' ')
    if 'up' in tmp:
        aim-=int(tmp[1])
    elif 'down' in tmp:
        aim+=int(tmp[1])
    elif 'forward' in tmp:
        hor+=int(tmp[1])
        ver+=(aim*int(tmp[1]))
print(hor*ver)