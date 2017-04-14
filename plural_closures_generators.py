import re
#A closure
def build_match_and_apply_functions(pattern, search, replace):
	def match_rule(word):
		return re.search(pattern, word)
	def apply_rule(word):
		return re.sub(search, replace, word)
	return (match_rule, apply_rule) 

def rules(rules_filename):
	with open(rules_filename, encoding = 'utf-8') as f:
		for line in f:
			pattern, search, replace = line.split(None, 3)
			yield build_match_and_apply_functions(pattern, search, replace)
			
def plural(noun, rules_filename = 'plural-rules.txt'):
	for match_rule, apply_rule in rules(rules_filename):
		if match_rule(noun):
			return apply_rule(noun)
	raise valueError('no matching rule for {0}'.format(noun))
	
if '__main__' == __name__:
	print('Finally, its successful!! yay!!!')
	print(plural('dash'))
	print(plural('latency'))
	print(plural('success'))
	print(plural('yay'))
	
