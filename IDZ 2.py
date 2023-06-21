words = ["щас", "чавель", "щашка", "щенок", "щасть", "четка"]

for word in words:
    if "ча" in word and "ща" not in word:
        new_word = word.replace("ча", "ща")
        print(f"Error detected in {word}. Corrected to {new_word}.")
    elif "ща" in word and "ча" not in word:
        new_word = word.replace("ща", "ча")
        print(f"Error detected in {word}. Corrected to {new_word}.")
    else:
        print(f"{word} is correct.")