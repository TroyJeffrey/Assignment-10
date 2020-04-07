# Troy Jeffrey Amegashie
# Assignment 10 - Modified Palindrome Check
# 04-06-2020


def palindrome_check(string):
    string.lower()

    if len(string) == 0 or len(string) == 1:
        print("Yes it is")
        return True

    elif string[0] != string[-1]:
        print("No it isn't")
        return False

    else:
        return palindrome_check(string[1:-1])


def punctuation_strip(string):
    string.strip()
    newLine = ""
    if not string.isalpha():
        for char in string:
            if char.isalpha():
                newLine+=char
        palindrome_check(newLine)


while True:

    word = str(input("Enter a word or a phrase and I'll tell you if it's a palindrome.\n>"))

    if not word.isalpha():
        punctuation_strip(word)

    else:
        palindrome_check(word)
