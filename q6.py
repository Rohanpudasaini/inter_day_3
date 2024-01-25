# 6. Create a list with the names of friends and colleagues. Search for the
# name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.

names = ["Rohan","John1", "Ganesh","Kushal","Sakar","Sweta"]

result ="Found" if (len(list(filter(lambda x: x=="John", names)))) != 0 else "Not Found"
print(result)