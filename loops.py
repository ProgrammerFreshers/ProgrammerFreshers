# Python program to illustrate
# while loop
count = 0
while (count < 3):   
    count = count + 1
    print("Hello ")
count = 0
while (count < 3):   
    count = count + 1
    print("Hello ")
else:
    print("In Else Block")
# Python program to illustrate
# Iterating over range 0 to n-1
 
n = 4
for i in range(0, n):
    print(i)
# Python program to illustrate
# Iterating by index
 
list = ["ahst", "for", "meen"]
for index in range(len(list)):
    print (list[index])
# Python program to illustrate
# nested for loops in Python
from __future__ import print_function
for i in range(1, 5):
    for j in range(i):
         print(i, end=' ')
  print()
    Prints all letters except 'e' and 's'
for letter in 'deeplearnings':
    if letter == 'e' or letter == 's':
         continue
    print 'Current Letter :', letter
    var = 10
or letter in 'deeplearnings':
 
    # break the loop as soon it sees 'e'
    # or 's'
    if letter == 'e' or letter == 's':
         break
 
print 'Current Letter :
# An empty loop
for letter in 'deeplearnings':
    pass
print 'Last Letter :', letter

fruits = ["apple", "orange", "kiwi"]
 
for fruit in fruits:
 
 print(fruit)