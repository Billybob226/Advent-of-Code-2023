



allnumberlist = []

file = open('AoC_1-1in.txt', 'r')
for line in file:
    decodedlist = []
    stringlist=[]
    string = line.strip()
    for char in string:
        stringlist.append(char)
    for char in stringlist:
        if char.isnumeric():
            decodedlist.append(int(char))
        
    list_size = len(decodedlist)

    if list_size == 1:
        first_num = decodedlist[0]
        tens = first_num*10
        finalnum = tens+first_num

    else:
        first_num = decodedlist[0]
        last_num = decodedlist[-1]
        tens = first_num*10
        finalnum = tens + last_num

    allnumberlist.append(int(finalnum))
code = 0 
for i in range(0, len(allnumberlist)):
    code = code + allnumberlist[i]

print(allnumberlist)
print('The secret elf code is ' +str(code))



