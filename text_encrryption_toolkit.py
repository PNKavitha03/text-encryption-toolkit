class TextEncryptionToolkit:
    def _init_(self):
        self.history = []

    def caesar_encrypt(self, text, shift):
        result = ""
        for ch in text:
            if ch.isalpha():
                base = ord('A') if ch.isupper() else ord('a')
                result += chr((ord(ch) - base + shift) % 26 + base)
            else:
                result += ch

        self.history.append(("ENCRYPT", text, result))
        return result

    def caesar_decrypt(self, text, shift):
        result = ""
        for ch in text:
            if ch.isalpha():
                base = ord('A') if ch.isupper() else ord('a')
                result += chr((ord(ch) - base - shift) % 26 + base)
            else:
                result += ch

        self.history.append(("DECRYPT", text, result))
        return result

    def rot13(self, text):
        result = ""
        for ch in text:
            if ch.isalpha():
                base = ord('A') if ch.isupper() else ord('a')
                result += chr((ord(ch) - base + 13) % 26 + base)
            else:
                result += ch

        self.history.append(("ROT13", text, result))
        return result

    def reverse_text(self, text):
        result = text[::-1]
        self.history.append(("REVERSE", text, result))
        return result

    def letter_frequency(self, text):
        freq = {}
        for ch in text.lower():
            if ch.isalpha():
                freq[ch] = freq.get(ch, 0) + 1

        self.history.append(("COUNT", text, freq))
        return freq

    def show_history(self):
        print("\n===== HISTORY =====")
        for item in self.history:
            print(item)


toolkit = TextEncryptionToolkit()

while True:
    print("\nTEXT ENCRYPTION TOOLKIT")
    print("1. Caesar Encrypt")
    print("2. Caesar Decrypt")
    print("3. ROT13")
    print("4. Reverse Text")
    print("5. Letter Frequency Counter")
    print("6. Show History")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        text = input("Enter text: ")
        shift = int(input("Enter shift value: "))
        print("Encrypted:", toolkit.caesar_encrypt(text, shift))

    elif choice == "2":
        text = input("Enter text: ")
        shift = int(input("Enter shift value: "))
        print("Decrypted:", toolkit.caesar_decrypt(text, shift))

    elif choice == "3":
        text = input("Enter text: ")
        print("ROT13:", toolkit.rot13(text))

    elif choice == "4":
        text = input("Enter text: ")
        print("Reversed:", toolkit.reverse_text(text))

    elif choice == "5":
        text = input("Enter text: ")
        print("Frequency:", toolkit.letter_frequency(text))

    elif choice == "6":
        toolkit.show_history()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
