class Solution:
    def reverseVowels(self, s: str) -> str:
        indexes=[]
        vowels = ['a', 'e', 'i', 'o', 'u']


        for i in range(len(s)):
            if s[i].lower() in vowels:
                indexes.append(i)
        print(f"{indexes=}")


        start = 0
        end = len(indexes)-1
        while(start < end):
            s = s[:indexes[start]] + s[indexes[end]] + s[indexes[start]+1: indexes[end]] + s[indexes[start]] + s[indexes[end]+1:]
            start += 1
            end -= 1
        print(f"{s=}")
        return s




s = "a."
obj = Solution()
obj.reverseVowels(s)
