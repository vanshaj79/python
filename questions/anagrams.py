words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = []

while words:
    removed_word = words.pop(0)   # hamesha first le lo
    group = [removed_word]

    clone = words[:]
    for w in clone:
        if sorted(w) == sorted(removed_word):
            group.append(w)
            words.remove(w)   # asli words list se hatao

    result.append(group)

print(result)
