# 5. Create a tuple with your first name, last name, and age. Create a list,
# people, and append your tuple to it. Make more tuples with the
# corresponding information from your friends and append them to the
# list. Sort the list. When you learn about sort method, you can use the
# key parameter to sort by any field in the tuple, first name, last name,
# or age.

person = []
tuple1 =("Rohan","Pudasaini",23)
tuple2 =("Ganesh","Kunwar",22)
tuple3 =("Kaushal","Gautam",18)
tuple4 =("Sakar","Poudel",8)

person.append(tuple1)
person.append(tuple2)
person.append(tuple3)
person.append(tuple4)
print(person)

sorted_first_name = sorted(person, key=lambda x:x[0])
sorted_last_name = sorted(person, key=lambda x:x[1])
sorted_age = sorted(person, key=lambda x:x[2])
print(sorted_first_name)
print(sorted_last_name)
print(sorted_age)