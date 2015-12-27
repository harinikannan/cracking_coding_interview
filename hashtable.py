
class item:
	key = ''
	item = 0

	def __init__(self, key, value):
		self.key = key
		self.value = value

	def print_kvpair(self):
		print("key: " + str(self.key) + "\n value: " + str(self.value))

class Hashtable:
	tableSize = 0
	numEntries = 0
	hashtable = [] #this is the actual hashtable

	def __init__(self, size):
		self.tableSize = size #note, that this does not actually create list of any size
		self.hashtable = [[] for i in range (size)]

	#Hash function	
	def hash(self, key):
		return ord(key) % self.tableSize;

	def insert(self, item):
		h = self.hash(item.key)
		hashed_list = self.hashtable[h]
		for i in hashed_list:
			if i.key == item.key:
				#delete the item if it already exists because you want to replace it
				del self.hashtable[h][i]
				self.numEntries -= 1
		#append the item to the end of the list
		self.hashtable[h].append(item)
		self.numEntries +=1

	def delete(self, key):
		h = self.hash(key)
		hashed_list = self.hashtable[h]
		for i in range (len(hashed_list)):
			if hashed_list[i].key == key:
				del hashed_list[i];
				self.numEntries -= 1
	
	def get(self, key):
		h = self.hash(key)
		for i in self.hashtable[h]:
			if i.key == key:
				return i
		return -1
					
	def print_table(self):
		for li in self.hashtable:
			for item in li:
				print ("\n key: " + str(item.key) + "\n value: " + str(item.value) + " ")

if __name__ == "__main__":
	hs = Hashtable(10)

	itm1 = item('h', 19)
	hs.insert(itm1);

	itm2= item('a', 26)
	hs.insert(itm2);

	itm3 = hs.get('h')
	#itm3.print_kvpair()

	hs.delete('h')
	hs.print_table()
	print (str(hs.numEntries))


