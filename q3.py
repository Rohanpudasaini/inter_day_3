# 3. Write code that will print out the anagrams (words that use the same
# letters) from a paragraph of text.

paragraph = '''man is nam and nad car rac is si anm'''.strip().split(" ")
# Check similar length words and check amongs them.
dict1 = {}
# dict1.po
test2 = []
for word in paragraph:
    empty_list = []
    for chr in word:
        if chr not in empty_list:
            empty_list.append(chr.lower())
    if word not in dict1:
        # empty_list.sort()
        dict1[word] = empty_list
dict3 = dict1.copy()
# print(dict3 == dict1)
final_dict = {}
for key , list2 in dict3.items():
    dict2 = dict1
    key1 = key
    dict2.pop(key)
    # print(dict2)
    # print(key1)
    # list2.sort()
    for key2, test in dict2.items():
        if set(list2) == set(test):
            # print(list2, key1, key2)
            if key2 not in test2:
                if key1 not in final_dict:
                    final_dict[key1] = key2
                else:
                    final_dict[key1] = final_dict[key1] +" " + key2
                test2.append(key2)

# final_final_dict = final_dict
# for value in final_final_dict.keys 
print(final_dict)





