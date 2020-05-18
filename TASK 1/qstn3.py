list1 = [1,2,3,4,5,6,7]
print(list1)
even=[]
odd=[]
for i in list1:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print("The even list",even)
print("The odd list",odd)   
    


