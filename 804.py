def uniqueMorseRepresentations(words):
    MORSE = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

    seen = {
    "".join(MORSE[ord(c) - ord('a')] for c in word ) for word in words #?????????????????
    }

    print(seen)
    return len(seen)

list = ["gin", "zen", "gig", "msg"]
uniqueMorseRepresentations(list)
