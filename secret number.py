# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 15:27:50 2017

@author: Anna
"""

print('hello world')
print('I like 6.00.1x!')

#print('Hello!')
#for x in range(0,10,-2):
#    print(x)

#bobNum=0
#index = 0;
#s = 'obobobbobosbobbzboob'
#for x in s:
 #print('########')
 #print('letter: '+str(x))    
 #print('index: '+str(index)) 
# if x=='b':
 # print('=======> found b: '+str(index)) 
 # print('Searching for Bob')
 # if s[index+1]=='o' and s[index+2]=='b':  
  #    print('found BOB !!!')
 # else:
  #    print('Did not found BOB - moving to next letter')
 #print('########')  
# index=index+1


#bobNum=0
#index=0
#for x in s[:-2]:
 #  if x=='b' and s[index+1]=='o' and s[index+2]=='b':            
  #     bobNum+=1
  # index=index+1
#print('Number of times bob occurs is: '+str(bobNum))

print('Please think of a number between 0 and 100!')
low=0
high=100
ans=(high+low)//2
x='l'

while x=='h' or x=='l' or x== 'c' or x!='h':
    print('Is your secret number ' + str(ans) + '?')
    x=input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly. ')
    if x=='h':
        high=ans
        ans=(high+low)//2
    elif x=='l':
        low=ans
        ans=(high+low)//2
    elif x=='c':
        print('Game over. Your secret number was: '+ str(ans))
        break
    else:
        print('Sorry, I did not understand your input.')

























