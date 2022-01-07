class Solution:
     def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # 1단계: day별 최소 ticket 가격을 저장한 list 생성
        day_size = max(days)
        cost_point = costs[0] * day_size 
        dp = [0] + [cost_point] * day_size 

        # 2단계: list별로 ticket 
        duration_day = [1, 7, 30]

        for day in range(1, day_size + 1):
            if day not in days: 
                dp[day] = dp[day - 1] # when day no in days
                continue
            else: # when i in days (calcuating)
                dp[day] = min(costs[0] + dp[max(0, day-1)], costs[1] + dp[max(0, day-7)], costs[2] + dp[max(0, day-30)])         

        return dp[-1]
