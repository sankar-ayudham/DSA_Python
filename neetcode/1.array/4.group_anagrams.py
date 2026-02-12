# from collections import defaultdict
#
# def group_anagrams(strs):
#     res=defaultdict(list)
#
#     for s in strs:
#         sortedS="".join(sorted(s))
#         print(sortedS)
#         res[sortedS].append(s)
#     return list(res.values())
# print(group_anagrams(strs = ["act","pots","tops","cat","stop","hat"]))

strs = ["act","pots","tops","cat","stop","hat"]
from collections import defaultdict

result = defaultdict(list)
for s in strs:
    count = [0] * 26
    for ch in s:
        count[ord(ch) - ord('a')] += 1
    result[tuple(count)].append(s)
print(result)
print(list(result.values()))
