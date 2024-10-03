class Solution(object):
    def findMaxAverage(self, nums, k):
        total = sum(nums[:k])
        maxtotal = total
        for n in range(k, len(nums)):
            total += nums[n] - nums[n - k]
            maxtotal = max(maxtotal, total)
        return float(maxtotal) / k
        