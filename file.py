
# open file
myFile=open('myFile.txt','w+')
# get some information
print('name:', myFile.name)
print('is closed:',myFile.closed)
print('opening mode:',myFile.mode)
# write to file
myFile.write(' i love python')
myFile.write(' i am java')
myFile.close()
# append to file
myFile= open('myFile.txt','W')
myFile.Write(' i also like php')
myFile.close()
# read from file
myFile=open('myFile.txt','r+')
text=myFile.read(12)
print(text)
