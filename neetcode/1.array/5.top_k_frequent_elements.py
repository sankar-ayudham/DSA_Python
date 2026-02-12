def topKelements(nums,k):
    count={}
    freq=[[] for i in range(len(nums)+1)]

    for num in nums:
        count[num]=1+count.get(num,0)
    for num,cnt in count.items():
        freq[cnt].append(num)

    res=[]
    for i in range(len(freq)-1,0,-1):
        for num in freq[i]:
            res.append(num)
            if len(res)==k:
                print(count,freq)
                return res

print(topKelements(nums = [5,5,5,12,12,3], k = 2))
