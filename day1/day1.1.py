file = open('example.txt', 'r')

values = []
num = 0

for line in file:
    line = line.strip('\n')
    print(line)
    values.append(line)

print(values)

for value in values:

    x = value[num].isdigit()
    # print(x)

    if x == True:
        print(value[num] + ' is True')
        num = 0

    else:
        print(value[num] + ' is False')
        num +=1
   
