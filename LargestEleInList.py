#------------------------------------------------Question-----------------------------------------------------
# Print the Largest Element in the List
#-------------------------------------------------------------------------------------------------------------


lst = []
n = int(input("Enter number of elements : ")) 
print("Enter all elements in order : ")

for i in range(0, n): 
    ele = int(input()) 
    lst.append(ele)

print("This is the entered list : \n"+str(lst)) 

lst.sort()

print("The Largest Element in the List = "+str(lst[-1]))