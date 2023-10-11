my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
sorted_keys = sorted(my_dict, key=my_dict.get, reverse=True)
top_3_keys = sorted_keys[:3]
print(top_3_keys)