# two words are said to be anagrams if it has same characters with same frequency but arranged in different order
def check_anagram(str1,str2):
   str1=str1.replace(" ","").lower()
   str2=str2.replace(" ","").lower()
   return sorted(str1)==sorted(str2)
print(check_anagram("list en","s  ilent"))