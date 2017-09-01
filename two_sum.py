unsorted_array = [1, 4, 5, 7, 3, 8, 9, 2]
two_pair_sum = 10
hashmap = {item:  0 for item in unsorted_array}
pair = list()
for item in unsorted_array:
		if two_pair_sum-item in hashmap and hashmap[two_pair_sum-item]:
			pair.append((item, two_pair_sum - item))
		hashmap.update({item : 1})
print(pair)


