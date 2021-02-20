# returns true of the array contains 007 in that order

def spy_game(nums):
  for number in nums:
    if number == 0:
      index = nums.index(number)
      if nums[index + 1] == 0 and nums[index + 2] == 7:
        return True
      else:
        return False

print spy_game([1,2,4,0,0,7,5])
print spy_game([1,0,2,4,0,5,7])
print spy_game([1,7,2,0,4,5,0]) 