'''
Created on Sep 11, 2015

@author: STEP
'''
#d=int(input("Input the starting day (0=Sun, 1=Mon, 2=Tues, 3=Weds, 4=Thurs, 5=Fri, 6= Sat, 7=Funday):"))
def main():
    n=int(input("Input the number of days in the month (28-31):  " )) #Asking the user for number of days in a month
    while n>31 or n<28:
        print("Please enter no more than 31 days and no less Than 28")
        n=int(input("Input the number of days in the month (28-31):  " ))
    else:
        d=int(input("Input the starting day (0=Sun, 1=Mon, 2=Tues, 3=Weds, 4=Thurs, 5=Fri, 6= Sat, 7=Funday):")) #Asking the user to input starting day of the week.
   
               
    for j in range(d):
        print("  ",end=" ")
    i=1
    while i <=n:
        if i < 10:
            print(" "+str(i), end=" ") #to line up the single digit numbers. 
        else:
            print (i, end=" ")# to line up all the double digit numbers.
        if (i+d) % 8==0:
            print(" ")
        i=i+1
    
main()