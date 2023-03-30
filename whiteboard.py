# Given a string of letters, write a function to see if the word  (case insensitive) is a palindrome (the same word spelled forward and backwards).
# The given string will contain only letters
# Examples:
# is_palindrome("RaceCar") \\ => True
# is_palindrome("mom")  \\ => True
# is_palindrome("Shoha") \\ => False

    # if odd(len(string)), check first and last are same and "2nd and 2nd last" are same, and so on and last(middle) can be anything
    # if even(len(string)), check first and last are same and "2nd and 2nd last" are same, and so on 
    # this approach is calles 2 pointer approach

def is_palindrom(word):
    word = word.lower()
    left = 0
    right = len(word)-1
    while left < len(word)//2:
        while word[left] == ' ':
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True

is_palindrom("racercar")

