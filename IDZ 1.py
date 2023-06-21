sentence = "The quick brown fox jumps over the lazy dog"
char1 = "o"
char2 = "e"

for i in range(len(sentence)):
    if sentence[i] == char1:
        for j in range(i+1, len(sentence)):
            if sentence[j] == char2:
                print(char1 + char2, "found at index", i, "and", j)
    elif sentence[i] == char2:
        for j in range(i+1, len(sentence)):
            if sentence[j] == char1:
                print(char2 + char1, "found at index", i, "and", j)