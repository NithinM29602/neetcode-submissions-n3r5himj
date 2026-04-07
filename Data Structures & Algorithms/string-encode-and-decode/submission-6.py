class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        str_len, res = [], ""

        for each_str in strs:
            str_len.append(len(each_str))
            res += str(len(each_str))
            res += ','
        res += "#"
        for each_str in strs:
            res += each_str
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        str_len, results, i = [], [], 0
        while s[i] != "#":
            cur = ""
            while s[i] != ",":
                cur += str(s[i])
                i +=1
            str_len.append(int(cur))
            i += 1
        i += 1
        for each_str_len in str_len:
            results.append(s[i:i+each_str_len]) 
            i += each_str_len
        return results
        
            


