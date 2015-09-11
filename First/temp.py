'''
Created on Sep 10, 2015

@author: STEP
'''
#===============================================================================
# def somefuction():
#     mystring= 'I am happy tomorrow is friday'
#     b=mystring.count('a')
#     print(b, end=' ')
#     print(b, end=' ')
#     
# somefuction()
#===============================================================================

'''def alist():
    Mylist=[5,7,9,"Bob","Apple", 11, 15.0]
    for a in Mylist:
        print(a)
    names=Mylist.pop(3)
    print("")
    print('________')
    print("this person failed the class", names)
    for a in Mylist:
        print(a)

alist()'''        


'''def atuple():
    
    myTuple = (1,2,3)
    myList = list(myTuple)
    myList.append(4)
    myTuple2=tuple(myList)
    print("this tuple can not be changed", myTuple)
    print ("so i turned it into a list and added an entry", myList)
    print("I then converted the list into a new tuple", myTuple2)
    
atuple()

def atuple():
    myTuple = (1,2,3)
    myList = list(myTuple)
    myList.append('Salad')
    B=Mylist.index('Salad',)
    myTuple2=tuple(myList)
    print("this tuple can not be changed", myTuple)
    print ("so i turned it into a list and added an entry", myList)
    print("I then converted the list into a new tuple", myTuple2)
    print(B)
atuple()'''

def exceptioncontrol():
    yoursmart=0
    while(yoursmart==0):
        try:
            a=int(input("Tell me your age as an integer "))
            print("you were born in the year ", 2015-a)
            yoursmart=1
        except:
            print("you did not enter an integer") 
exceptioncontrol()

