class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        p=defaultdict(int);
        for i in nums:
            p[i]+=1

        n=[]
        s_p=dict(sorted(p.items(),key=lambda item:item[1],reverse=True))
        for i in s_p:
            n.append(i)
            k-=1
            if k==0:
                break
                k-=1
        return n


