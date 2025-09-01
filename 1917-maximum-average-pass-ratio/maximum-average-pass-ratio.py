class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        def calculate_gain(p, t):
            return float(p + 1) / (t + 1) - float(p) / t
        max_heap = []
        for p, t in classes:
            if p == t:
                gain = 0
            else:
                gain = calculate_gain(p, t)
            heapq.heappush(max_heap, (-gain, p, t))
        for _ in range(extraStudents):
            neg_gain, p, t = heapq.heappop(max_heap)
            p += 1
            t += 1
            if p == t:
                new_gain = 0
            else:
                new_gain = calculate_gain(p, t)
            heapq.heappush(max_heap, (-new_gain, p, t))
        total_ratio = 0
        for neg_gain, p, t in max_heap:
            total_ratio += float(p) / t  
        return total_ratio / len(classes)