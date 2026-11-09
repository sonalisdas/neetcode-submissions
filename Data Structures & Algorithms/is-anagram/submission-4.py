class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        p,q={},{}
        for i in s:
            if i in p:
                p[i]+=1
            else:
                p[i]=1
        for j in t:
            if j in q:
                q[j]+=1
            else:
                q[j]=1
        return p==q


