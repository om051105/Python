from collections import Counter

text = "RAM is RAM"
words = text.split()
word_count = Counter(words)

for word, count in word_count.items():
    print(f"{word} repeated {count} time")