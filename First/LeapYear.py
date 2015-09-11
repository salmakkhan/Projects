'''
Created on Sep 11, 2015

@author: STEP
'''


def main():
    year= int(input("Enter A year: "))
    print("\n")
    if(year%4==0 and year%100!=0):
        print("Leap year")
    elif(year % 4==0 and year%100==0):
        if(year%400==0):
            print("Leap Year")
        else:
            print("Not a Leap Year")
    
    else:
        print("not a leap year") 
main()