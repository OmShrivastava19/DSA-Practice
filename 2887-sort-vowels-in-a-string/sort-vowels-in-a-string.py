class Solution(object):
    def sortVowels(self, s):
        vowels_set = set('aeiouAEIOU')
        extracted_vowels = []
        for char in s:
            if char in vowels_set:
                extracted_vowels.append(char)
        extracted_vowels.sort()
        result_list = list(s)
        vowel_pointer = 0
        for i in range(len(result_list)):
            if result_list[i] in vowels_set:
                result_list[i] = extracted_vowels[vowel_pointer]
                vowel_pointer += 1
        return "".join(result_list)