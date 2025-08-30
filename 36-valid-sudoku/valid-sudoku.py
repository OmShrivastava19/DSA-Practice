class Solution(object):
    def isValidSudoku(self, board):
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        # Iterate through every cell on the board
        for r in range(9):
            for c in range(9):
                digit = board[r][c]
                # Skip empty cells
                if digit == ".":
                    continue
                # Calculate the index for the 3x3 sub-box
                box_index = (r // 3) * 3 + (c // 3)
                # Check for duplicates
                if digit in rows[r] or digit in cols[c] or digit in boxes[box_index]:
                    return False
                # If no duplicate, add the digit to our records
                rows[r].add(digit)
                cols[c].add(digit)
                boxes[box_index].add(digit)
        # If the loops complete, no duplicates were found
        return True