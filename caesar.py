def caesar_cipher(text, shift, mode):
    result = ""

    # Menyesuaikan pergeseran untuk mode dekripsi
    if mode == "decrypt":
        shift = -shift

    for char in text:
        # Mengecek huruf besar
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Mengecek huruf kecil
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Jika karakter bukan huruf, tambahkan langsung
            result += char

    return result

# Menu interaktif
if __name__ == "__main__":
    print("Caesar Cipher Program")
    mode = input("Pilih mode (encrypt/decrypt): ").lower()
    text = input("Masukkan teks: ")
    shift = int(input("Masukkan pergeseran (shift): "))

    if mode in ["encrypt", "decrypt"]:
        result = caesar_cipher(text, shift, mode)
        print(f"Hasil {mode}: {result}")
    else:
        print("Mode tidak valid. Pilih 'encrypt' atau 'decrypt'.")

