nums = [1,2,3,1,2,3]
k = 2
i = 0
boo = "true"
n = 0
r = nums[n:k + n + 1]
for i in range(len(nums) - 1):
    if nums.count(nums[i]) > 1 and nums[i] in r:
                
        print("t",nums[i] ,n, r)
        boo = "true"
        print(boo)
    else:
        print("f",nums[i], n, r)
        boo = "false"

    
    n += 1        
    r = nums[n:k + n + 1]
print(boo)