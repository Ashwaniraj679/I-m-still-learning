def skip_elements(elements):
	# code goes here
	lst1 = []
	index = 0
	for index, elem in enumerate(elements, index):
		if int(index) % 2 ==0 :
			lst1.append(elem)
		
	return lst1

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']