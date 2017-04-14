# Write a method that takes in a string. Return the longest word in
# the string. You may assume that the string contains only letters and
# spaces.
#
# You may use the String `split` method to aid you in your quest.
#
# Difficulty: easy.
def longest_word(sentence):
	main_list = []
	word_list = sentence.split(' ')
	longest_w = len(word_list[0])
	for i in range(0, len(word_list)):
		word_len = len(word_list[i])
		word_len_list = [word_list[i], len(word_list[i])]
		main_list.append(word_len_list)
		if word_len > longest_w:
			longest_w = word_len
	longest = [w for [w,l] in main_list if l == longest_w]
	longest_str = ''.join(longest)
	return longest_str
  
# These are tests to check that your code is working. After writing
# your solution, they should all print true.

if __name__ == '__main__':
	print("\nTests for #longest_word")
	print("===============================================")
	print(longest_word("short longest") == "longest")
	print(longest_word("one") == "one")
	print(longest_word("abc def abcde") == "abcde")
	print("===============================================")