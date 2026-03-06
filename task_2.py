def search_word_in_file():

    word = input("Введите слово для поиска: ").strip()

    found = False
    count = 0
    lines_with_word = []

    try:
        with open("text.txt", "r", encoding="utf-8") as file:
            for i, line in enumerate(file, start=1):
                if word in line:
                    found = True
                    count += line.count(word)
                    lines_with_word.append(i)
    except FileNotFoundError:
        print("Файл 'text.txt' не найден.")
        return


    if found:
        print(f"Слово '{word}' найдено.")
        print(f"Количество вхождений: {count}")
        print(f"Номера строк с словом: {lines_with_word}")
    else:
        print(f"Слово '{word}' не найдено.")

    with open("search_results.txt", "w", encoding="utf-8") as output_file:
        if found:
            output_file.write(f"Слово '{word}' найдено.\n")
            output_file.write(f"Количество вхождений: {count}\n")
            output_file.write(f"Номера строк: {lines_with_word}\n")
        else:
            output_file.write(f"Слово '{word}' не найдено.\n")

if __name__ == "__main__":
    search_word_in_file()