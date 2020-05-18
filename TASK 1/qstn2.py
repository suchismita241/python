inputStr = "proGRamMiNg"
words = inputStr.split()
lower = []
upper = []
for char in inputStr:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
sortedString = ''.join(lower + upper)
print(" arranging characters where lowercase letters occurs first:")
print(sortedString)
         
           


