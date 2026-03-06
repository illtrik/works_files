def combine_files_with_custom_separators():
    input_files = ["file1.txt", "file2.txt", "file3.txt"]
    output_file = "combined.txt"

    with open(output_file, "w", encoding="utf-8") as outfile:
        for filename in input_files:
            try:
                with open(filename, "r", encoding="utf-8") as infile:
                    outfile.write(f"=== Содержимое {filename} ===\n")
                    content = infile.read()
                    outfile.write(content)
                    outfile.write("\n\n")
            except FileNotFoundError:
                print(f"Внимание! Файл {filename} не найден и пропущен.")

if __name__ == "__main__":
    combine_files_with_custom_separators()