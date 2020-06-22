'''1119. Remove Vowels from a String
Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.
Example 1:

Input: "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
Example 2:

Input: "aeiou"
Output: ""
'''

class Solution:
    @staticmethod
    def removeVowels(str):
        #write code here
        return


if __name__ == '__main__':
    print("Test Case1 :" + Solution.removeVowels("leetcodeisacommunityforcoders"))
    assert(Solution.removeVowels("leetcodeisacommunityforcoders")) == 'ltcdscmmntyfrcdrs'
    print("Test Case2 :" + Solution.removeVowels("aeiou"))
    assert(Solution.removeVowels("aeiou")) == ''
