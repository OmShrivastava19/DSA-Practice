class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        MOD = 10**9 + 7
        daily_log = [0] * (n + 1)
        daily_log[1] = 1
        sharing_count = 0
        for day in range(2, n + 1):
            day_to_start_sharing = day - delay
            if day_to_start_sharing >= 1:
                sharing_count = (sharing_count + daily_log[day_to_start_sharing]) % MOD
            day_to_forget = day - forget
            if day_to_forget >= 1:
                sharing_count = (sharing_count - daily_log[day_to_forget] + MOD) % MOD
            daily_log[day] = sharing_count
        total_aware = 0
        for i in range(n - forget + 1, n + 1):
            total_aware = (total_aware + daily_log[i]) % MOD            
        return total_aware