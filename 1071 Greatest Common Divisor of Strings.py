class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2) < len(str1):
            str1, str2 = str2, str1 
        res = ""
        for i in range(1, len(str1)+1):
            sub_str = str1[0:i]
            if str2.replace(sub_str, "") == "" and str1.replace(sub_str, "") == "":
                res = sub_str
        return res
        