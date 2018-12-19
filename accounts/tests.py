from django.test import TestCase

# Create your tests here.
def is_palindrome(word):
    #Please write your code here.
    index = 0

    for i in word:
        #print i
        #print word[-index]
        index+=1

        if i.upper() != word[-index].upper():

            return False

    return True

print is_palindrome('Deleveled')
x='abc'
#print x[-3]

