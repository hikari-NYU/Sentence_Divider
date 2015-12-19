from nltk.corpus import cmudict as cd

#Dividing string to a sequence of words
#@Input: dictionary: The word corpus used; string: The sentence to divide
#@Output: The required string with whitespaces dividing words
def divider(dictionary,string):
	#Fit to the dictionary which contains only lower case words
	string=string.lower()
	#A list to be popped from back
	charStack=[]
	for i in range(len(string)):
		charStack.append(string[i])
	#A list of legal words
	wordList=[]
	candidate=''
	csLength=len(charStack)
	while csLength>0:
		#Flag showing if the tail's bound to a letter preceding it.
		#If not, the end of one word.
		modified=False
		j=len(charStack)
		maxW=''
		while j>0:
			j=j-1
			candidate=string[j]+candidate
			if candidate in dictionary:
				if len(candidate)>len(maxW):
					maxW=candidate
					modified=True
		if modified==False:
			#End of word
			maxW=charStack[-1]
		#Append word into word list
		wordList.append(maxW)
		candidate=''
		#Remove tail from original sentence
		for i in range(len(maxW)):
			del charStack[-1]
		#Update length of list to traverse
		csLength=len(charStack)
	#Reverse the words in the list and join them to be one string, then return
	return ' '.join(wordList[::-1])

def main():
	dictionary=[]
	for entry in cd.entries():
		dictionary.append(entry[0])
	sent=''
	while sent!='EXIT':
		sent=raw_input("Input the sentence you want to divide('EXIT' to exit):")
		if sent!='EXIT':
			print divider(dictionary,sent)

if __name__=="__main__":
	main()