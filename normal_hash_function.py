hashTable=[[] for i in range(10)] #ninjatechnique to create matrix
def display(hashTable):
	for i in range(len(hashTable)):
		print(i,end=" ")
		for j in hashTable[i]:
			print("-->",end=" ")
			print(j,end=" ")
		print()
	

def get_key(hashKey):
	return hashKey%10
def insert(hashTable,hashKey,value):
	key=get_key(hashKey)
	hashTable[key].append(value)

insert(hashTable,10,"allahbad")
insert(hashTable,9,"Noida")
insert(hashTable,20,"aligarh")
insert(hashTable,19,"agra")
display(hashTable)


