class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        sorted_counts = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
        most_frequent = []
        for tup in range(k):
            most_frequent.append(sorted_counts[tup][0])
        return most_frequent
