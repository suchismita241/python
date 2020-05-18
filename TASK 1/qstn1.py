def outerFun(a, b):
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    def innerFun(a,b):
        return a+b
    add = innerFun(a, b)
    return add+5

result = outerFun(5, 10)
print(result)
         
           


