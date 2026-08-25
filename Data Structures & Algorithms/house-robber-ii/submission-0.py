class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 3:
            return max(nums)
        n1 = nums[:-1]
        n2 = nums[1:]

        dp1 = n1[0]
        dp2 = max(n1[0], n1[1])


        for i in range(2, len(n1)):
            t = max(dp1+n1[i], dp2)
            dp1 = dp2
            dp2 = t
        res = max(dp1, dp2)
        dp1 = n2[0]
        dp2  = max(n2[0], n2[1])

        for j in range(2, len(n2)):
            temp = max(dp1+n2[j], dp2)
            dp1 = dp2
            dp2 = temp
        return max(res, dp1, dp2)
