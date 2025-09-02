class Solution(object):
    def numberOfPairs(self, points):
        n = len(points)
        valid_pair_count = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 <= x2 and y1 >= y2:
                    is_empty = True
                    for k in range(n):
                        if k == i or k == j:
                            continue   
                        x3, y3 = points[k]
                        if x1 <= x3 <= x2 and y2 <= y3 <= y1:
                            is_empty = False
                            break
                    if is_empty:
                        valid_pair_count += 1
        return valid_pair_count