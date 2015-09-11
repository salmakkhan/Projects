'''
Created on Sep 10, 2015

@author: STEP
'''
def somefuction():
    mystring= 'I am happy tomorrow is friday'
    b=mystring.count('a')
    print(b, end=' ')
    print(b, end=' ')
    
somefuction()

def alist():
    Mylist=[5,7,9,"Bob","Apple", 11, 15.0]
    for a in Mylist:
        print(a)
    Mylist.reverse()
    print("")
    print('________')
    for a in Mylist:
        print(a)

alist()        