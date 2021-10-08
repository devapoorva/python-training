# reverse order of words 
# Ram is a good boy
# boy good a is Ram

s = input("enter string ")
words = s.split() # list
rev_words = []
i = len(words)-1

while i >=0:
    rev_words.append(words[i])
    i = i-1

reversed = " ".join(rev_words)
print(reversed)



