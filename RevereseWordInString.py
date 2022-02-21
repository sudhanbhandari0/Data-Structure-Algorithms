class Solution:
    def reverseWords(self, s: str) -> str:
        
        newS = s.split(" ")
        s1=""

        for i in range(len(newS)):
            
            s1+=newS[i][::-1]
            
            if (i < (len(newS))-1):
                s1+=" "
        
        return s1
        