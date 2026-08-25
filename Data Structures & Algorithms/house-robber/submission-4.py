class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        elif len(nums)<=3:
            return max(max(nums), nums[0]+nums[2])

        dp = [nums[0], nums[1], nums[0]+nums[2]]
        for i in range(3, len(nums)):
            dp2 = dp[2]
            dp[2] = max(dp[0], dp[1]) + nums[i]
            dp[0] = dp[1]
            dp[1] = dp2
        return max(dp)

        # [2,9,8,3,6,2,9,8,3,6]
        #          i
        #          result = max(p(i-2), p(i-3))+i