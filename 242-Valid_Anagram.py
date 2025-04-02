class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #Checking if the length of the string the same or not, if not then it's not a match. So it should return as false.
            return False
        
        counter = {}
        for char in s: 
            #Looping in each character of string, and assign it into counter (hash) and see if at counter there is the char, if not then it will return 0 as defaul and +1 after that to show, the main purpose are to count how much each character are in the string, example "a" : 1
            counter[char] = counter.get(char,0) + 1
        
        for char in t:
            if char not in counter or counter[char] == 0:
                return False
            else:
                counter[char] -= 1
        return True
        #Looping each character again, and then checks if the char not in counter, or the "char" == 0, it means there is no that huruf on the counter (which is the previous string). Then if there is the same char on counter (previous string), the counter["char"] will decreased. For example "b" : 1. Because there is b on second string, it will be "b" : 0. If all character was the same, it will return true. It means that it's valid as anagram
