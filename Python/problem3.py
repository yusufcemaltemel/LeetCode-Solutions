class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
     
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            # Eğer sağdaki karakter setin içindeyse, soldakileri çıkararak pencereyi daralt
            while s[right] in char_set:
             char_set.remove(s[left])
             left += 1
        
         # Karakteri ekle ve yeni uzunluğu hesapla
            char_set.add(s[right])
            current_window_size = right - left + 1
            max_length = max(max_length, current_window_size)

        return max_length
