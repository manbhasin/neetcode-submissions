class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}
        s_chars = list(s)
        t_chars = list(t)

        for char in s_chars:
            s_dict[char] = s_dict.get(char, 0) + 1

        for char in t_chars:
            t_dict[char] = t_dict.get(char, 0) + 1

        is_all_same = True

        for data in s_dict:
            if s_dict.get(data) != t_dict.get(data):
                is_all_same = False
                break;
        
        return is_all_same
        
