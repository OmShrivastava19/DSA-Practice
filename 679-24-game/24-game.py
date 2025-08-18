class Solution(object):
    def judgePoint24(self, cards):
        float_cards = [float(c) for c in cards]
        return self.can_solve(float_cards)

    def can_solve(self, numbers):
        if len(numbers) == 1:
            return abs(numbers[0] - 24) < 1e-6

        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                a = numbers[i]
                b = numbers[j]
                
                remaining = [numbers[k] for k in range(len(numbers)) if k != i and k != j]
                
                possible_results = {a + b, a * b, a - b, b - a}
                if b != 0:
                    possible_results.add(a / b)
                if a != 0:
                    possible_results.add(b / a)
                
                for res in possible_results:
                    if self.can_solve(remaining + [res]):
                        return True
        
        return False