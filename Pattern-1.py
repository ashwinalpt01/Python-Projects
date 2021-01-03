#----------------------------------------------Question-----------------------------------------------------------
#1
#232
#34543
#4567654
#567898765
#----------
#-----------

#Print the above pattern by taking the No. of Steps to be printed as Input

#-----------------------------------------------------------------------------------------------------------------


def pat(n):
    i=1
    
    while i<=n:
        j=1
        k=i
        preval=i-1
        
        while j<=((2*i)-1):
            print(k,end='')
            if (preval<k)and(k<((2*i)-1)):
                preval=k
                k=k+1
            else:
                preval=k
                k=k-1
            j=j+1
        i=i+1
        print("\n") 

n=int(input("Enter No. of Lines of Pattern to be Printed : "))
pat(n)