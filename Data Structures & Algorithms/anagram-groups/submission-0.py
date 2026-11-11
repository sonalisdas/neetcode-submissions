class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        p= defaultdict(list)

        for i in strs:
            a=[0]*26
            for q in i:
                a[ord(q)-ord('a')]+=1
            p[tuple(a)].append(i)
        return list(p.values())