class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort() #sorting the numbers / interger on the list
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]: #checking if number i (example the first is 1) the same or not with number i-1 (example 0) if same then return True, if it keeps not getting true, then return false. After iterate into all len list
                return True
        return False
