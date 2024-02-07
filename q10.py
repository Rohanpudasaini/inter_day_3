
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
            new_string += j.lower()
            continue
        if j.isupper():
           new_string = new_string + seperator +j.lower()
        #    print(new_string)
           continue
        new_string += j
    return new_string

#ganesh's solution
# import re
# @get_time
# def camel_to_snake(camel_string,separator='_'):
#     # find all capital letter in the string and replace them with the seperator followed by their lowercase  equivalent
#     snake_string=re.sub(r'(?<=[a-z])(?=[A-Z])',separator,camel_string)

#     # make first character of the string to lower
#     snake_string=snake_string[0].lower() +snake_string[1:]

#     return snake_string


# print(convert_case(string="HelloWorldHowAreYou"))
# print(convert_case_e(string="HelloWorldHowAreYou"))
print(convert_case_e(string="HelloWorldHowAreYou", seperator="-"))
# print(convert_case_e(string="HelloWorldHowAreYou", seperator=" "))
# print(convert_case_e(string="HelloWorldHowAreYou", seperator="~"))
# print(camel_to_snake(camel_string="HelloWorldHowAreYou", separator="-"))
         
        
