nums = [1,1,0,1,0,1,1,0]
k = 2
ind = 0
for i in range(len(nums) - k + 1):
    ones = nums[i:i + k]
    print(ones)
    if sum(ones) == k:
        ind+=1
    else:
        None
    print(ones)