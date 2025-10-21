"""
Word Occurrences
Estimate: 20 minutes
Actual: 30 minutes
"""


word_count = {}
text = input("Text: ").split()
for word in text:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

max_length = max(len(word) for word in word_count)
for word, count in sorted(word_count.items()):
    print(f"{word:{max_length}} : {count}")

