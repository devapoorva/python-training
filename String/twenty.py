# reverse internal content of each words 
# Ram is a good boy
# maR si a doog yob

s = input("Enter string ")
words = s.split()
rev_words = []
i = 0

while i < len(words):
    w = words[i]
    rev = w[::-1]
    rev_words.append(rev)
    i = i+1

output = " ".join(rev_words)
print(output)
