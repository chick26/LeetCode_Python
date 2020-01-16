class Solution:
    def lengthOfLongestSubstring(self, s: str):
        Cur_string=''
        String_Num=max_length=0
        if s is None: return 0
        for i in range(len(s)):             #遍历字符串
            String_Num+=1                   #读取到第一个字符，字符串长度增一
            while Cur_string.find(s[i])>=0: #当当前连续无重复字串中有当前遍历的字符
                Cur_string=Cur_string[1:]   #移除字符串最左侧字符，直至无重复项,eg:pwwwkew
                String_Num-=1               #每移除一次，字段长度减一
            Cur_string+=s[i]                #加入当前字符
            if max_length<String_Num:       #存取最大长度
                max_length=String_Num
        return max_length

s="abcabcbb"
Solution=Solution()
print(Solution.lengthOfLongestSubstring(s))