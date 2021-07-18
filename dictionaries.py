# simple dictionary
person ={'frist_name':'john','last_name':'doe','age':32}


perint(person)
# using a constructor
person=dict( frist_name='john',last_name='doe',age=32)
print(person)
# Access value
print(person['frist_name'])
print (person.get(('last_name'))
# add keys
person['contact_number']='1234567890'
print(person)
#get keys
print(person.keys())
#get items
print(person.items())
print(person.items())
print(person)
# make copy
person2=person.copy()
person2['city']='boston'
print(person2)
# remove items
del(person['age'])
print(person)
# clear
person.clear()
# get length
print(len(person2))
print(person)
#list of dict
people=[{ 'name':'meen','age':23},{ 'name':'bob,'age':23'}]
print(people[2])
