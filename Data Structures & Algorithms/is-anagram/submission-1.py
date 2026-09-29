class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = 0
        letter_count = {}
        if len(s) == len(t): 
            for char in s:
                if char not in letter_count: 
                    letter_count[char] = 1
                else: 
                    letter_count[char] = letter_count[char] + 1
            for char in t: 
                if char not in letter_count: 
                    return False

                if char in letter_count: 
                    letter_count[char] = letter_count[char] - 1

                    if letter_count[char] == -1: 
                        return False
        else: 
            return False        
        return True   


                 
            

    