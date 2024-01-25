# 4. Create a list. Append the names of your colleagues and friends to it.
# Has the id of the list changed? Sort the list. What is the first item on
# the list? What is the second item on the list?

initial_list = []
print(id(initial_list))

initial_list.append("Rohan")
initial_list.append("Ganesh")
initial_list.append("Kaushal")

print(id(initial_list))

# print(id(initial_list[0]))
# print(id(initial_list[1]))


initial_list.append("Rohan")
initial_list.append("Ganesh")
initial_list.append("Kaushal")

print(id(initial_list))
initial = id(initial_list)

# print(id(initial_list[0]))
# print(id(initial_list[1]))

def add1():
    initial_list.append("Rohan")
    initial_list.append("Ganesh")
    initial_list.append("Kaushal")
count  =0
while True:
    add1()
    count +=1
    if initial != id(initial_list):
        print(count)
        break
    if count == 1000000000000000000000:
        break



