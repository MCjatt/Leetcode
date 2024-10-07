class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        
        boo = 0
        n = 0
        r = nums[n:k + n + 1]
        for i in range(len(nums) - 1):
            if r.count(nums[i]) >= 2 and nums[i] in r and len(nums) > 1:
                
                #print("t",nums[i] ,n, r, nums.count(nums[i]))
                boo = 1
                return boo
            else:
                boo = 0
                #print("f",nums[i], n, r)
            
            n += 1
            r = nums[n:k + n + 1]
        return boo