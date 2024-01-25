# 14. Write a function that reads a CSV file. It should return a list of
# dictionaries, using the first row as key names, and each subsequent
# row as values for those keys.
# For the data in the previous example it would return:
# [{'name': 'George', 'address': '4312 Abbey Road', 'age': 22}, {'name':
# 'John', 'address': '54 Love Ave', 'age': 21}]
import os
import csv
file_name = "Hello"
final_list = []
def read_csv(file_name:str) -> list:
    if file_name+".csv" in os.listdir():
        temp = 1
        with open(file_name+".csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if temp == 1:
                    temp = 0
                    header = row
                    continue
                # dict1 = {header[0]:row[0],header[2]:row[2],header[2]:row[2]}
                dict1 = {header[x]:row[x] for x in range(len(header))}
                final_list.append(dict1)
                # print(row)
        return(final_list)
    return f"No file with name {file_name} in current directory"