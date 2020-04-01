#created on 31/03/2020, 9:38
#author:samuvel
from collections import Counter 
a=input("enter the elements of the series with space after each entry:") #getting input from user
list=a.split()# sliping and eliminating white space to get elements
print("list of array you entered",list)# printing to make sure the inputs are correct
 
def main(): 
    dictOfElems = dict(Counter(list)) #creating new variable and using counter from collection library 
    dictOfElems = { key:value for key, value in dictOfElems.items() if value > 0} # to collect the info of element and num of times the value get repeted
 
    for key, value in dictOfElems.items(): #using for loop to give number of outputs for the given entry
            print('Element' , key , 'Repeated', value,'times')  # printing the output
   
 
if __name__ == '__main__':
    main()# calling the function


