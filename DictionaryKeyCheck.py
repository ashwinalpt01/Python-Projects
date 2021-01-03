#-----------------------------------------Question--------------------------------------------
# Program to Check Whether a particular key is present in the input Dictonary
#---------------------------------------------------------------------------------------------

n=int(input("No. of Entries required in the Dictionary : "))
key=[]
val=[]
dict={}

for i in range(0,n):
    key_ele=input("Enter the Key : ")
    key.append(key_ele)
    val_ele=input("Enter the Corresponding Value : ")
    val.append(val_ele)
    dict[key_ele]=val_ele
    

reqd_key = input("Enter the key to be Checked : ")
k=0

for i in dict:
    if i==reqd_key:
        print("Key is Present")
        k=1
        break
if k==0:
     print("Key is not Present")
        
print("The Created Dictionary : \n",dict)