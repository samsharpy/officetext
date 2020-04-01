#created on 01/04/2020, 7:13
#author:samuvel
list=[]#creating list for sum
a=0#naming the variable a and b for the storing of the values of batsman 1 and 2
b=0
over=int(input("enter the number of overs: "))#geting number of overs to clculate number balls bowled
overtoballs=over*6#multiplaying 6 with overs to get balls 
print ("number of balls is:",overtoballs)#printing the number of balls
print("enter the scores accuired in each ball pressing 'enter' and leave blank if no balls bouled")
for i in range(overtoballs):
    try:
        score=int(input("enter the runs accuired in ball:"))#getting the runs in single ball for looping in number of balls
        list.append(score)#updating list with runs
    except:    
        if score==str:#eluminating space and charaters
            continue
print(list)# printing the runs in list



sum=0
for num in list:
    sum+=int(num)
print("total=",sum)#prnting the total score by adding elements of the list

for s in list:#rtaking s as the run and using for loop to oprate all runs in the list
    if s==4 :
        a+=s
        continue
    elif s==2:
        a+=s
        continue
    elif s==6:
       a+=s
       continue
    elif s==0:#getting 4,6,2,0 as the  same score of the  batsman in srike as he cant change his position 
       a+=s
       continue
    else:
        b+=s
        continue
#getting runs of both batmans to print
a=a
b=b

        
print("batsman1=",a)
print("batsman2=",b)

