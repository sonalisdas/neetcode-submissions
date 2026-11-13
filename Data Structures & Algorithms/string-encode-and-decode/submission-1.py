class Solution:

    def encode(self, strs: List[str]) -> str:

        res=''
        for i in strs:
            res+=str(len(i))+'#'+i
        return res

    def decode(self, s: str) -> List[str]:

        res=[]
        i=0
        while(i<len(s)):
            length=''
            j=i
            while(s[j]!='#'):
                length=length+s[j]
                j+=1
            res.append(s[j+1:j+1+int(length)])
            i=j+1+int(length)
        return res