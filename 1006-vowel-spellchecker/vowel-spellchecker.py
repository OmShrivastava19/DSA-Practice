class Solution(object):
    def spellchecker(self, wordlist, queries):
        v="aeiou" #for vowels
        exact=set(wordlist)
        cap={} #for capital diff
        for w in wordlist: #for each word
            l=w.lower() #making the word in lower case
            if l not in cap:
                cap[l]=w    
        vowel={} # when vowel differ
        for w in wordlist:
            pattern=""
            for c in w.lower(): #checking characters
                if c in v: #if character is a vowel
                    pattern+="*" #show vowels in both string look *
                else:
                    pattern+=c
            if pattern not in vowel:
                vowel[pattern]=w
        r=[] #result array
        for q in queries:
            if q in exact: #when exact 
                r.append(q)
            elif q.lower() in cap:#when lowercase making the diff
                r.append(cap[q.lower()])
            else: #vowel difference case
                p=""
                for c in q.lower():
                    if c in v:
                        p+="*"
                    else:
                        p+=c
                if p in vowel:
                    r.append(vowel[p])
                else:
                    r.append("")
        return r #returning the result