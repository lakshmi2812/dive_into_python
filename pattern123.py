def pattern123(nums):
  x = 0
  pattern = False
  while x < len(nums)-2:
    if nums[x] == 1 and nums[x+1] == 2 and nums[x+2] == 3:
      pattern = True
      break
    x+=1
  return pattern