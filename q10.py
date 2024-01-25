
# 10. Write a function that takes camel-cased strings (i.e.
# ThisIsCamelCased), and converts them to snake case (i.e.
# this_is_camel_cased). Modify the function by adding an argument,
# separator, so it will also convert to the kebab case
# (i.e.this-is-camel-case) as well.
from get_time import get_time

# @get_time
# def convert_case(string:str,seperator:str = "_"):
#     new_string = ""
#     count = 0
#     for j in string:
#         # print(j.isupper())
#         if count == 0:
#             new_string += j
#             count = 1
#             continue
#         if j.isupper():
#            new_string = new_string + seperator +j
#         #    print(new_string)
#            continue
#         new_string += j
#     return new_string

@get_time
def convert_case_e(string:str,seperator:str = "_"):
    new_string = ""
    for i, j in enumerate(string):
        if i == 0:
            new_string += j
            continue
        if j.isupper():
           new_string = new_string + seperator +j
        #    print(new_string)
           continue
        new_string += j
    return new_string


# print(convert_case(string="HelloWorldHowAreYou"))
print(convert_case_e(string="HelloWorldHowAreYou"))
print(convert_case_e(string="HelloWorldHowAreYou", seperator="-"))
print(convert_case_e(string="HelloWorldHowAreYou", seperator=" "))
print(convert_case_e(string="HelloWorldHowAreYou", seperator="~"))

         
        
