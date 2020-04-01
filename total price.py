#created on 31/03/2020 , 9:27
#author:samuvel
a={}# declating an empty variable with dictionary entry

n=int(input("enter the number of entries:"))#geting num of set of entries 

for i in range(n):#with n looping for number of n times to get the values
      k=str(input("enter the name:" ))#string value for name 
      v=int(input("enter the price:"))#integer value for values 
      a.update({k:v})# updating the name and there values to  variable 'a'

sum=0 #declaring a variable sum=0
for num in a.values():#geting entries of values only to sum 
    sum+=int(num)
print("total=",sum)#getting sum and printing as total in output
print(a)   #printing 'a' to show the user the entire list of the entries

