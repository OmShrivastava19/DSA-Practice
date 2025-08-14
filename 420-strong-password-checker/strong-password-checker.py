class Solution(object):
    def strongPasswordChecker(self, password):
        n = len(password)
        
        missing_type = 3
        if any(c.islower() for c in password): missing_type -= 1
        if any(c.isupper() for c in password): missing_type -= 1
        if any(c.isdigit() for c in password): missing_type -= 1

        # SCENARIO 1: Password is too short
        if n < 6:
            return max(6 - n, missing_type)

        # Calculate initial replacements and get a list of all repeat lengths
        replacements = 0
        repeats = []
        i = 0
        while i < n:
            j = i
            while j < n and password[j] == password[i]:
                j += 1
            repeat_len = j - i
            if repeat_len >= 3:
                replacements += repeat_len // 3
                repeats.append(repeat_len)
            i = j
            
        # SCENARIO 2: Password length is good
        if n <= 20:
            return max(replacements, missing_type)
        
        # SCENARIO 3: Password is too long
        else:
            deletions = n - 20
            
            # Use deletions to reduce the number of replacements needed.
            # 1 deletion on a seq of len L where L%3==0 saves 1 replacement.
            # We track this by subtracting from the total replacements.
            replacements_saved = 0
            
            # Use 1 deletion on each L%3==0 sequence
            for i in range(len(repeats)):
                if deletions > 0 and repeats[i] % 3 == 0:
                    deletions -= 1
                    replacements_saved += 1
            
            # Use 2 deletions on each L%3==1 sequence
            for i in range(len(repeats)):
                if deletions > 1 and repeats[i] % 3 == 1:
                    deletions -= 2
                    replacements_saved += 1
            
            # Any remaining deletions can be used 3 at a time to reduce replacements
            if deletions > 0:
                replacements_saved += deletions // 3

            # The final replacements needed is the initial count minus what we saved.
            # But we can't save more replacements than we initially needed.
            final_replacements = max(0, replacements - replacements_saved)
            
            # The total steps are the mandatory deletions plus the remaining fixes.
            return (n - 20) + max(missing_type, final_replacements)