class Solution(object):
    def minOperations(self, queries):    
        def calculate_total_cost(n):
            if n == 0:
                return 0
            total_cost = 0
            power_of_4 = 1
            while power_of_4 <= n:
                total_cost += (n - power_of_4 + 1)
                if power_of_4 > n // 4:
                    break
                power_of_4 *= 4                
            return total_cost
        total_operations_sum = 0
        for l, r in queries:
            range_cost = calculate_total_cost(r) - calculate_total_cost(l - 1)
            operations_for_query = (range_cost + 1) // 2            
            total_operations_sum += operations_for_query     
        return total_operations_sum