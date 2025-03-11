class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        s = list(s)  # Convert the string to a list for easy swapping
        left, right = 0, len(s) - 1

        while left < right:
            # Move left pointer until it finds a vowel
            while left < right and s[left] not in vowels:
                left += 1
            # Move right pointer until it finds a vowel
            while left < right and s[right] not in vowels:
                right -= 1
            
            # Swap the vowels
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return ''.join(s)

s = "IceCreAm"
obj = Solution()
obj.reverseVowels(s)
