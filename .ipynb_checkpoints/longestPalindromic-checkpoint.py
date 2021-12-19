
s="zxtpipiprte"

def longestPalindrome(s):
	myDict = {}
	for i,l in enumerate(s):
		print("#1: ", i, l)
		if l in myDict.keys():
			inds = myDict[l]
			myDict.append(i)
		else:
			myDict[l] = []
			myDict[l].append(i)
		print("####\n", myDict)


longestPalindrome(s)
