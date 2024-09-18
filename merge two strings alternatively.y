class Solution:
    def mergeAlternately(self,word1,word2):
        result=""
        i=0
        j=0
        n1=len(word1)
        n2=len(word2) 
        while i<n1 and j<n2:
            result+=word1[i]+" "+word2[i]+" "
            i+=1
            j+=1
        while i<n1:
            result+=word1[i]+" " 
            i+=1   
        while j<n2:
            result+=word2[j]+" "   
            j+=1 
        return result    
word1=input()
word2=input()
s=Solution()    
res=s.mergeAlternately(word1,word2)   
print(res)  