from string import punctuation

def words_count(text: str) -> dict:
    for interp in punctuation:
        text = text.replace(interp, "")

    words = text.lower().split()
    print(words)

    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

text = "this? is cat. Is, Cat ;Cat"
result = words_count(text)
print(result)
