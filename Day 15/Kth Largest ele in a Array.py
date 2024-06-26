from heapq import heapify, heappush, heappop 
def findKthLargest(nums, k):
        minHeap = []
        heapify(minHeap)

        for ele in nums:
            heappush(minHeap, ele)
            if len(minHeap) > k:
                heappop(minHeap)
        return minHeap[0]
nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(findKthLargest(nums,k))