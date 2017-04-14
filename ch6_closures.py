#CLOSURES
import re
def build_match_and_apply_functions(pattern, search, replace):
	def match_rule(word):
		return re.search(pattern, word)
	def apply_rule(word):
		return re.sub(search, replace, word)
	return (match_rule, apply_rule)
	

patterns = \
		(
			('[sxz]$', '$', 'es'),
			('[^aeioudgkprt]h$', '$', 'es'),
			('[^aeiou]y$', 'y$', 'ies'),
			('$', '$', 's')
		)

rules = [build_match_and_apply_functions(pattern, search, replace) for (pattern, search, replace) in patterns]

def plural(noun):
	for (match_rule, apply_rule) in rules:
		if(match_rule(noun)):
			return apply_rule(noun)
			
if __name__ == '__main__':
	print(plural('push'))
	print(plural('vacancy'))
	print(plural('shark'))
	print(plural('blush'))
	
	
	

		