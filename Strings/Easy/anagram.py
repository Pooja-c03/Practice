# Check if 2 strings are anagram or no

#from collection package

from collections import Counter

def anagram(s1,s2):
    if len(s1) != len(s2):
        print("Not Anagram.")
    else:
        if Counter(s1) == Counter(s2):
            print("Anagram.")
        else:
            print("Not Anagram.")

if __name__=="__main__":
    s1 = input("Enter 1st string: ")
    s2 = input("Enter 2nd string: ")
    anagram(s1,s2)

# using sorted fn

def sort(s1,s2):
    if sorted(s1) == sorted(s2):
        print("Anagram.")
    else:
        print("Not Anagram.")

if __name__=="__main__":
    s1 = input("Enter 1st string: ")
    s2 = input("Enter 2nd string: ")
    sort(s1,s2)