class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}

        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        arr=[]

        sorted_items=sorted(freq.items(),key=lambda x:x[1],reverse=True)

        for num,count in sorted_items[:k]:
            arr.append(num)
        return arr

        