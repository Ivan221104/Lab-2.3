sentence = input("Введите предложение: ")
letter = input("Введите букву, которую нужно вставить: ")

if "и" in sentence:
    new_sentence = sentence.replace("и", letter + "и", sentence.count("и") - 1)
    print(f"Измененное предложение: {new_sentence}")
else:
    print("В предложении нет буквы 'и'.")