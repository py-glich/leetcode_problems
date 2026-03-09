class Solution:
    def lengthOfLongestSubstring(self,word:str)->int:
        seen={}
        left=0
        max_len=0
        for right ,char in enumerate(word):
            if char in seen and seen[char]>=left:
                left=seen[char]+1
            seen[char]=right
            max_len=max(max_len,right-left+1)
        return max_len
obj=Solution()
substring=obj.lengthOfLongestSubstring("pwwhew")
print(substring)