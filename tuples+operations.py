point = (23, 56, 11)
DNAsequence= (“atatatatatata”, “gcgcgcgcgcgcg”, “atgcatgc”)
JSS_Coordinates=(12.3428N,76.6525E)
#Indexing
first_list = [1, 2, 3, 4, 5]
print (first_list[0])
print (first_list[-1])

first_tuple = (1, 2, 3, 4, 5)
print (first_tuple[0])
print (first_tuple[-1])


#To access an element that is inside a sequence
seqdata = (’MRVLLVALALLA’, 12, ’5FE9EEE8EEa2DC2C7’)
seqdata[0][5]     ’V’

#Slicing
my_sequence="Python"
my_sequence[0:4]     ’Pyth’
my_sequence[:2]     ’Py’
my_sequence[4:]     ’ on’
my_sequence[0:4:2]     ’Pt’

for x in first_list:
	print x

for index_no, element_value in enumerate(first_list):
	print index_no, "\t", element_value 
