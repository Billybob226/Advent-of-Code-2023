with open('AoC_1-1in.txt', 'r') as file:
    sum = 0
    nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    reverseNums = ['orez', 'eno', 'owt', 'eerht', 'ruof', 'evif', 'xis', 'neves', 'thgie', 'enin']
    
    for line in file:
        print('Line: {}'.format(line), end='')
        firstNum = ''
        lastNum = ''
        for index, c in enumerate(line):
            if not firstNum:
                if c.isdigit():
                    firstNum = firstNum + c
                else:
                    for num in nums:
                        if num in line[index:index + len(num)]:
                            firstNum = firstNum + str(nums.index(num))

        reverseLine = line[::-1]
        print('Reverse Line: ' + reverseLine)

        for index, c in enumerate(reverseLine):
            if not lastNum:
                if c.isdigit():
                    lastNum = lastNum + c
                else:
                    for reverseNum in reverseNums:
                        if reverseNum in reverseLine[index:index + len(reverseNum)]:
                            lastNum = lastNum + str(reverseNums.index(reverseNum))
                            print(reverseNums.index(reverseNum))
                        
        print()
        print('First Num: ' + firstNum)
        print('Last Num: ' + lastNum)
        print('First Num + Last Num: ' + firstNum + lastNum)
        sum += int(firstNum + lastNum)
        print("Sum: " + str(sum))
    print(sum)
