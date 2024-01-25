# 13. Write a function to write a comma-separated value (CSV) file. It
# should accept a filename and a list of tuples as parameters. The
# tuples should have a name, address, and age. The file should create
# a header row followed by a row for each tuple. If the following list of
# tuples was passed in:
# [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]

# it should write the following in the file:

# name,address,age
# George,4312 Abbey Road,22
# John,54 Love Ave,21
import os
import csv
# current_dir  = os.listdir()
# if file_name+".csv" in current_dir:
#     print("Filename already exsist.")
#     exit()
# file_name = input("Enter the filename to create: ")
tupl_list = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
def make_csv(file_name:str, tupl_list:list) -> str:
    if not file_name+".csv" in os.listdir():
        temp = 0
        with open(file_name+".csv","w") as file:
            # writer = file.w
            writer = csv.writer(file)
            if temp == 0:
                writer.writerow(["Name", "Address", "Age"])
            writer.writerows(tupl_list)
        return(f"sucessfully created a csv with name {file_name}")
    else:
        return(f"Filename {file_name} already exsist.")

print(make_csv("Hello", tupl_list))
