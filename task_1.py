def main():
    input_file = 'resourse/input.txt'
    output_file = 'resourse/statistics.txt'

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    num_lines = len(lines)
    num_words = 0
    for line in lines:
        words = line.split()
        num_words += len(words)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f'Количество строк: {num_lines}\n')
        f.write(f'Количество слов: {num_words}\n')

if __name__ == '__main__':
    main()
