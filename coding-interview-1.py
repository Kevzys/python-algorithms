#Write an efficient function that checks whether any permutation of an input string is a palindrome.

def isPalindrome(string):

    included_letters = set()

    for letter in string:
        if letter in included_letters:
            included_letters.remove(letter)
        else:
            included_letters.add(letter)

    return len(included_letters) <= 1


string = 'civic'
string2 = 'civci'
string3 = 'ciivi'
string4 = 'aaa'
string5 = 'aabb'
string6 = 'aaaabbcc'

print(isPalindrome(string))
print(isPalindrome(string2))
print(isPalindrome(string3))
print(isPalindrome(string4))
print(isPalindrome(string5))
print(isPalindrome(string6))
