
colortotal = [12, 13, 14]
colors = ['red', 'blue', 'green']


redballs = 0
blueballs = 0
greenballs =0

code = 0
GameID = 0
file = open('AoC_day2ex.txt', 'r')
for line in file:
    readstring = []
    red_total = 0
    blue_total =0
    green_total = 0
    GameID +=1
    testString = line.strip()
    for char in testString:
        readstring.append(char)
    for i in range(len(readstring)):
        if readstring[i] == 'r' and i >= 2 and readstring[i - 2].isdigit():
            red = int(readstring[i - 2])
            redballs = 0
            redballs += red
        elif readstring[i] == 'b' and i >= 2 and readstring[i - 2].isdigit():
            blue = int(readstring[i - 2])
            blueballs = 0 
            blueballs += blue
        elif readstring[i] == 'g' and i >= 2 and readstring[i - 2].isdigit():
            green = int(readstring[i - 2])
            greenballs = 0 
            
            greenballs += green
        elif readstring[i] == ';':
            red_total += redballs
            blue_total += blueballs
            green_total += greenballs
            redballs = 0
            blueballs = 0
            greenballs = 0 
        elif i == (int(len(readstring))-1):
            red_total +=redballs
            blue_total +=blueballs
            green_total+=greenballs
            
            if red_total > 12 or blue_total > 13 or green_total > 14:
                   print("Fail")
            elif red_total <= 12 and blue_total <= 13 and green_total <=  14:
                print("Game", GameID, "Success ")
            
                code += GameID

print(code)
        
    
        
        
    
                      
