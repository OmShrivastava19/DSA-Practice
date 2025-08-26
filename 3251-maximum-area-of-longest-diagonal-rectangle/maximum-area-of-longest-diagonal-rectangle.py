class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        max_diagonal_sq = 0
        max_area = 0      
        for length, width in dimensions:
            current_diagonal_sq = length**2 + width**2
            if current_diagonal_sq > max_diagonal_sq:
                max_diagonal_sq = current_diagonal_sq
                max_area = length * width
            elif current_diagonal_sq == max_diagonal_sq:
                max_area = max(max_area, length * width)
        return max_area