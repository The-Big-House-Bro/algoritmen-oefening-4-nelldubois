def countTargetPairs(nums, target):
    aantal = 0
    lengte = len(nums)
   
    for i in range(lengte):
        for j in range(i + 1, lengte):
            if nums[i] + nums[j] < target:
                aantal += 1
   
    return aantal


voorbeeld1 = countTargetPairs([-1, 1, 2, 3, 1], 2)  
voorbeeld2 = countTargetPairs([-6, 2, 5, -2, -7, -1, 3], -2)  

print(voorbeeld1)  
print(voorbeeld2)