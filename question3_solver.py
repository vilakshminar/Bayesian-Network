import re

class Question3_Solver:
	def __init__(self, cpt):
		self.cpt = cpt;
		self.hiddencpt = []
		mycpt = cpt
		for p in range(2):
			newcpt = []
			alpha = '`abcdefghijklmnopqrstuvwxyz'
			for x in range(len(alpha)):
				tempcpt = []
				for y in range(len(alpha)):
					if p == 0:
						temp = sum([self.cpt.conditional_prob(alpha[w], alpha[x]) * self.cpt.conditional_prob(alpha[y], alpha[w]) for w in range(len(alpha))])
					else:
						temp = sum([mycpt[x][w] * self.cpt.conditional_prob(alpha[y],alpha[w]) for w in range(len(alpha))])
					tempcpt.append(temp)
				newcpt.append(tempcpt)
			mycpt = newcpt
			self.hiddencpt.append(newcpt)
	#####################################
	# ADD YOUR CODE HERE
	# Pr(x|y) = self.cpt.conditional_prob(x, y);
	# A word begins with "`" and ends with "`".
	# For example, the probability of word "ab":
	# Pr("ab") = \
	#    self.cpt.conditional_prob("a", "`") * \
	#    self.cpt.conditional_prob("b", "a") * \
	#    self.cpt.conditional_prob("`", "b");
	# 	query example:
	#  	  query: "qu--_--n";
	#    return "t";
	def solve(self, query):
		list_of_words = query.split('_')
		m = re.search('[-_]', query)
		dashword = query[m.start():]
		if re.search('[a-z]', dashword):
			n = re.search('[a-z]', dashword)
			dashword = dashword[0:n.start()]
		else:
			dashword = dashword[0:len(dashword)]
		preword = '`' + list_of_words[0]
		remword = list_of_words[1] + '`'
		l = len(preword)
		first = preword[len(preword)-1]
		last = remword[0]
		pr = 1
		if l > 1:
			for x in range(1, l):
				if preword[x] != '-':
					pr = pr * self.cpt.conditional_prob(preword[x], preword[x-1])
				else:
					first = preword[x-1]
					break
		tempword = preword.split('-')
		preword = tempword[0].split('_')[0]
		l = len(remword)
		if l > 1:
			for x in range(1, l):
				if remword[x-1] != '-':
					if last == '-':
						last = remword[x-1]
					pr = pr * self.cpt.conditional_prob(remword[x], remword[x-1])
				elif last == '-':
					last = remword[x]
		# Till now you have the start character before the first dash, end character after the last dash ---> first and last
		# Then you have the combination of dashs ---> dashword
		# You also have the probablities of the known character combinations
		# have to calculate the probablities of the hidden by summing up and the _ character
		alpha = 'abcdefghijklmnopqrstuvwxyz'
		best_prob = 0
		best_char = 'a'
		l = len(dashword)
		index = 0
		m = re.search('_', dashword)
		underscore = m.start()
		end = l-m.start()-1
		if first == '`':
			index = 0
		else:
			index = ord(first)-96
		if last == '`':
			lastindex = 0
		else:
			lastindex = ord(last)-96
		for x in range(len(alpha)):
			if m.start() == 0:
				temp = pr * self.cpt.conditional_prob(alpha[x], first) * self.hiddencpt[end-1][x+1][lastindex]
			elif m.start()+1 == len(dashword):
				temp = pr * self.hiddencpt[underscore-1][index][x+1] * self.cpt.conditional_prob(last,alpha[x]) 
			else:
				temp = pr * self.hiddencpt[underscore-1][index][x+1] * self.hiddencpt[end-1][x+1][lastindex]
			if best_prob < temp:
				best_prob = temp
				best_char = alpha[x]
		return best_char

