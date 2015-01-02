class Question2_Solver:
	def __init__(self, cpt):
		self.cpt = cpt;
		return;

	#####################################
	# ADD YOUR CODE HERE
	# Pr(x|y) = self.cpt.conditional_prob(x, y);
	# A word begins with "`" and ends with "`".
	# For example, the probability of word "ab":
	# Pr("ab") = \
	#    self.cpt.conditional_prob("a", "`") * \
	#    self.cpt.conditional_prob("b", "a") * \
	#    self.cpt.conditional_prob("`", "b");
	# query example:
	#    query: "que__ion";
	#    return ["s", "t"];
	def solve(self, query):
		word = query.split('_')
		word[0] = '`' + word[0]
		word[2] = word[2] + '`'
		pr = 1
		if len(word[0]) > 0:
			for x in range(1,len(word[0])):
				pr = pr * self.cpt.conditional_prob(word[0][x], word[0][x-1])
		if len(word[2]) > 0:
			for x in range(len(word[1])-1):
				pr = pr * self.cpt.conditional_prob(word[1][x+1],word[1][x])
		best_element = ['a', 'a']
		best_probablity = 0
		alpha = 'abcdefghijklmnopqrstuvwxyz'
		for x in range(len(alpha)):
			temp = pr * self.cpt.conditional_prob(alpha[x], word[0][len(word[0])-1])
			for y in range(len(alpha)):
				newtemp = temp * self.cpt.conditional_prob(alpha[y], alpha[x]) * self.cpt.conditional_prob(word[2][0], alpha[y])
				if best_probablity < newtemp:
					best_probablity = newtemp
					best_element = [alpha[x], alpha[y]]
		return best_element
