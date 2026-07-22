s = "Anishka Singh"

print("original String:", s)
print("Reversed String:", s[::-1])

reversed_words = " ".join(word[::-1] for word in s.split())
print("Each Word Reversed:", reversed_words)
