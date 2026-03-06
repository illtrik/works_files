def sort_words():
    try:
        with open("words.txt", "r", encoding="utf-8") as file:
            words = [line.strip() for line in file if line.strip()]

        sorted_alphabetically = sorted(words, key=str.lower)
        sorted_by_length = sorted(words, key=len)
        sorted_reverse = sorted(words, key=str.lower, reverse=True)

        with open("sorted_alphabetically.txt", "w", encoding="utf-8") as f:
            for word in sorted_alphabetically:
                f.write(word + "\n")

        with open("sorted_by_length.txt", "w", encoding="utf-8") as f:
            for word in sorted_by_length:
                f.write(word + "\n")

        with open("sorted_reverse.txt", "w", encoding="utf-8") as f:
            for word in sorted_reverse:
                f.write(word + "\n")

        print("Сортировка и запись в файлы успешно выполнены!")

    except FileNotFoundError:
        print("Файл 'words.txt' не найден. Проверь, пожалуйста, его наличие.")

if __name__ == "__main__":
    sort_words()