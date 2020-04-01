#created at 30/03/2020 ,  20:34;
#//author:samuvel
a=1# creating the variable with initial value
b=int(input('enter the ending number'))# geting value from the user where to stop
for i in range (a ,b+1):
    #using for loop from initial value and user input value (b+1) becuse loop index start from 0
    if i%3==0 and i%5==0:#finding the multiples of both 3 and 5
        print("FizzBuzz") #printing fizzbuzz 
    elif (i%5==0):# finding multible of 5
        print("Buzz")#printing buzz
    elif (i%3==0):#finding multiple of 3
        print("fizz")#printing fizz
    else:
        print(i) #printing other number
        
