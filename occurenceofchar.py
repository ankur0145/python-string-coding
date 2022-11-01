string=input("enter the string:")
char=input("enter the character:")
count=0
for i in range(len(string)):
    if(string[i]==char):
        count=count+1
print("number of times ocuurence",char,"is:",count)        
