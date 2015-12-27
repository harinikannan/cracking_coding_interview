from hashtable import *

def uniquecharacters(s):
	hs = Hashtable(len(s))

	for i in range(len(s)):
		is_inTable = hs.get(s[i])
		if (is_inTable != -1):
			return False
		itm = item(s[i],0)
		hs.insert(itm)
	return True

def unique_characters_sans_datastuct(s):
	for i in range(len(s)):
		if (s.count(s[i]) > 1):
			return False
	return True

def reverseString(s):
	newStr = ""
	for i in range(len(s)-1, -1, -1):
		newStr += s[i]
	return newStr

def replaceSpace(s):
	newStr = ""
	for i in range(len(s)):
		if (s[i] == " "):
			newStr += "%20"
		newStr += s[i]
	return newStr

def compressed(s):
	if(len(s) == 0):
		return ""
	if(len(s) == 1):
		return s + str(1);
	a = s[0]
	count = 0
	for i in range(len(s)):
		if s[i] == a:
			count +=1
	#print str(count)
	#print a + str(count)
	x = a + str(count) + compressed(s[count:len(s)]) 

	#print len(x)
	#print len(s)
	return x if len(x) <= len(s) else s

if __name__ == "__main__":
	#s1 = "harini"
	#u1 = uniquecharacters(s1)
	#print str(u1) + "\n"
	#usd1 = unique_characters_sans_datastuct(s1)
	#print str(usd1) + "\n"

	#s2 = "brian"
	#u2 = uniquecharacters(s2)
	#print str(u2) + "\n"
	#usd2 = unique_characters_sans_datastuct(s2)
	#print str(usd2) + "\n"

	#s = "aaron_ramsey"
	#print reverseString(s)

	#s = "aabbccdddd"
	#s = "aabbccd"
	#s = "aaaab"
	#s1 = "abbb"
	#print compressed(s)
	#print compressed(s1)
