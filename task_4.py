def caesar_encrypt(text, shift=3):
    result = []
    for char in text:

        if 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))

        elif 'а' <= char <= 'я':
            result.append(chr((ord(char) - ord('а') + shift) % 32 + ord('а')))
        elif 'А' <= char <= 'Я':
            result.append(chr((ord(char) - ord('А') + shift) % 32 + ord('А')))
        else:
            result.append(char)
    return ''.join(result)


def caesar_decrypt(text, shift=3):
    return caesar_encrypt(text, -shift)


def encrypt_file():
    try:
        with open("secret.txt", "r", encoding="utf-8") as fin:
            text = fin.read()

        encrypted_text = caesar_encrypt(text, 3)

        with open("encrypted.txt", "w", encoding="utf-8") as fout:
            fout.write(encrypted_text)

        print("Текст зашифрован и сохранён в encrypted.txt")

    except FileNotFoundError:
        print("Файл secret.txt не найден.")


def decrypt_file():
    try:
        with open("encrypted.txt", "r", encoding="utf-8") as fin:
            encrypted_text = fin.read()

        decrypted_text = caesar_decrypt(encrypted_text, 3)

        with open("decrypted.txt", "w", encoding="utf-8") as fout:
            fout.write(decrypted_text)

        print("Текст расшифрован и сохранён в decrypted.txt")

    except FileNotFoundError:
        print("Файл encrypted.txt не найден.")


if __name__ == "__main__":
    encrypt_file()
    decrypt_file()