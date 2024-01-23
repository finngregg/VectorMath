def addition(a,b):   
    c = []
    for i in range (0,3):
        c.append(eval(a[i])+eval(b[i]))
    return c
   
def dot(a,b):
    beg  = 0
    for i in range(0,3):
        beg += eval(a[i])*eval(b[i])
    return beg  

def norm_A(a,b):
    import math
    sum = 0
    for i in range(0,3):
        sum += eval(a[i])**2
    if sum == 0:
        return "0.00"
    else:
        return round(math.sqrt(sum),2)
    
def norm_B(a,b):
    import math
    sum = 0
    for i in range(0,3):
        sum += eval(b[i])**2
    if sum == 0:
        return "0.00"
    else:
        return round(math.sqrt(sum),2) 

def main():
    a = input("Enter vector A:\n")
    b = input("Enter vector B:\n")
    
    a = a.split()
    b = b.split()    
    
    print("A+B = "+str(addition(a,b)))
    print("A.B = "+str(dot(a,b)))
    print("|A| = "+str(norm_A(a,b)))
    print("|B| = "+str(norm_B(a,b)))

main()    