class Solution(object):
    def flowerGame(self, n, m):
        # Count even and odd numbers for the first lane (range 1 to n)
        n_even = n // 2
        n_odd = (n + 1) // 2

        # Count even and odd numbers for the second lane (range 1 to m)
        m_even = m // 2
        m_odd = (m + 1) // 2

        # Calculate the two winning scenarios and add them up
        winning_pairs = (n_even * m_odd) + (n_odd * m_even)

        return winning_pairs