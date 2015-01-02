class Question5_Solver:
    def __init__(self, cpt2):
        self.cpt2 = cpt2;
        return;

    #####################################
    # ADD YOUR CODE HERE
    #         _________
    #        |         v
    # Given  z -> y -> x
    # Pr(x|z,y) = self.cpt2.conditional_prob(x, z, y);
    #
    # A word begins with "``" and ends with "``".
    # For example, the probability of word "ab":
    # Pr("ab") = \
    #    self.cpt2.conditional_prob("a", "`", "`") * \
    #    self.cpt2.conditional_prob("b", "`", "a") * \
    #    self.cpt2.conditional_prob("`", "a", "b") * \
    #    self.cpt2.conditional_prob("`", "b", "`");
    # query example:
    #    query: "ques_ion";
    #    return "t";
    def solve(self, query):
	pr = 1
	temp_query = '``'+query+'``'
	ind = temp_query.index('_')
	parts = temp_query.split('_')
	f_part = parts[0]
	l_part = parts[1]

	len_fpart = len(f_part)
	len_lpart = len(l_part)

	f_word = temp_query[ind-2]+temp_query[ind-1]+temp_query[ind]+temp_query[ind+1]+temp_query[ind+2]

	for x in range(2, len_fpart):
		pr = pr * self.cpt2.conditional_prob(f_part[x], f_part[x-2], f_part[x-1])
	for x in range(2, len_lpart):
		pr = pr * self.cpt2.conditional_prob(l_part[x], l_part[x-2], l_part[x-1])

	alph = 'abcdefghijklmnopqrstuvwxyz'
	i = f_word.index('_')
	best_pr = float("-inf")

	for c in alph:
		f_pr = pr * self.cpt2.conditional_prob(c, f_word[i-2], f_word[i-1]) * self.cpt2.conditional_prob(f_word[i+1], f_word[i-1], c) * self.cpt2.conditional_prob(f_word[i+2], c, f_word[i+1])

		if f_pr > best_pr:
			best_pr = f_pr
			best_el = c

	return best_el

