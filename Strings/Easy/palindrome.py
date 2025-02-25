def palindrome(string):
    if string == string[::-1]:
        print("Palindrome")
    else:
        print("Not palindrome")

if __name__ == '__main__':
    string = input("Enter string of choice: ")
    palindrome(string)