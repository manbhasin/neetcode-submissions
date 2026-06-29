class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        s_chars = sorted(list(s))
        t_chars = sorted(list(t))

        for char in s_chars:
            s_dict[char] = s_dict.get(char, 0) + 1

        for char in t_chars:
            t_dict[char] = t_dict.get(char, 0) + 1

        is_same_length = (len(s_dict) == len(t_dict))

        if not is_same_length:
            return False

        is_all_same = True

        for data in s_dict:
            if s_dict.get(data) != t_dict.get(data):
                is_all_same = False
                break;
        
        return is_all_same
        
