# 7. Create a list of tuples of first name, last name, and age for your
# friends and colleagues. If you don't know the age, put in None.
# Calculate the average age, skipping over any None values. Print out
# each name, followed by old or young if they are above or below the
# average age.
from functools import reduce
my_age = 21

person = []
tuple1 =("Sakar","Poudel",8)
tuple2 =("Ganesh","Kunwar",22)
tuple3 =("Kaushal","Gautam",18)
tuple4 =("sweta", "Maharjan", "None")

person.append(tuple1)
person.append(tuple2)
person.append(tuple3)
person.append(tuple4)
total_sum = 0
# average = reduce(lambda x,y: total_sum+(x[2]+y[2]) if x[2] != "None" else total_sum+0, person)
# average = reduce(lambda accu, person:(accu+ person[2] if type(person[2] != type(1)) else 0 ) , person, 0)
average = reduce(lambda acc, person: acc + (person[2] if isinstance(person[2], int) else 0), person, 0)
# average = (reduce(lambda x, totalsum: total_sum + x[2] if x[2] != "None" else (total_sum + 0), person))
# def get_average(x)

old = list(map(lambda x: x[2]>my_age if isinstance(x[2], int) else "Not Known if", person)) 
for i in range(len(person)):
    print(f"Its {old[i]} {person[i][0]} is older than me")
# print(list(old))
print(average/len(person))
# for item in person:
#     average(item)
# print(total_sum)
