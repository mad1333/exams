#Функция возвращает true если строка - палиндром
def palindrome_cheker(text: str) -> bool:
    altered = "".join(
        char for char in text.casefold()
        if not char.isspace()
    )
    return altered == altered[::-1]

if __name__ == "__main__":
    text = input()
    print(palindrome_cheker(text))
