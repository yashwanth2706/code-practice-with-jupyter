def reverseInplace(nums):
  length = len(nums)
  ptr1 = 0
  ptr2 = length-1
  temp = 0
  while ptr1 < length//2:
    temp = nums[ptr1]
    nums[ptr1] = nums[ptr2]
    nums[ptr2] = temp
    ptr1 += 1
    ptr2 -= 1
  return nums
  reverseInplace([1,2,3,4,5,6,7,8,9,10])
