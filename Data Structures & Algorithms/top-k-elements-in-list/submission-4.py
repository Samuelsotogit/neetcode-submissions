class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
# Frequency bucket solution
        # counts = {}
        # for num in nums:
        #     counts[num] = counts.get(num, 0) + 1
        # buckets = [[] for _ in range(len(nums) + 1)]
        # for key, value in counts.items():
        #     buckets[value].append(key)
        # result = []
        # for i in range(len(buckets) - 1, 0, -1):
        #     if len(buckets[i]) == 0:
        #         continue
        #     for num in buckets[i]:
        #         result.append(num)
        #         if len(result) == k:
        #             return result
                
                

# Sorting Solution        
# # Time complexity: O(n X log(n)) because there are no inner loops and all loops iterate over n items worst case. The sort algorithm is O(n * log(n)).
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        sorted_counts = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
        return [pair[0] for pair in sorted_counts[:k]]
#         # most_frequent = []
#         # for tup in range(k):
#         #     most_frequent.append(sorted_counts[tup][0])
#         # return most_frequent
