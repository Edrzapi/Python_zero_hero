# smart way to remove duplicates in a list and retain order!

old_list = ["A", "C", "B", "C", "A",  "C"]
new_list = list(dict.fromkeys(old_list).keys())
print(new_list)

# comprehension

new_dict = {x:x for x in range(1,5)}
print(new_dict)
paired_dict = {x: [j for j in range(0, 5)] for x in range(1, 5)}
print(paired_dict)


new_list = [x for x in range(1,5)]
print(new_list)

new_set = {x for x in range(1,5)}
print(new_set)

new_tup = tuple(x for x in range(1,5)) # generator expression
# use a cast
print(new_tup)
