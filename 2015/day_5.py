def contains_3_vowels(str_: str) -> bool:
    """
    
    >>> contains_3_vowels("aei")
    True
    >>> contains_3_vowels("xazegov")
    True
    >>> contains_3_vowels("aeiouaeiouaeiou")
    True
    """
    number_of_vowels = 0
    for char in str_:
        if char in "aeiou":
            number_of_vowels += 1

    return number_of_vowels >= 3

def double_letter(str_: str) -> bool:
    """

    >>> double_letter("xx")
    True
    >>> double_letter("abcdde")
    True
    >>> double_letter("aabbccdd")
    True
    """
    previous_letter = str_[0]
    for char in str_[1:]:
        if char == previous_letter:
            return True
        
        previous_letter = char
    
    return False


def evil_strings(str_: str) -> bool:
    """

    >>> evil_strings("ab")
    True
    >>> evil_strings("cd")
    True
    >>> evil_strings("pq")
    True
    >>> evil_strings("xy")
    True
    """
    evils = {"ab", "cd", "pq", "xy"}
    for evil in evils:
        if evil in str_:
            return True

    return False



def nice(str_: str) -> bool:
    """https://adventofcode.com/2015/day/5
    
    >>> nice("ugknbfddgicrmopn")
    True
    >>> nice("aaa")
    True
    >>> nice("jchzalrnumimnmhp")
    False
    >>> nice("haegwjzuvuyypxyu")
    False
    >>> nice("dvszwmarrgswjxmb")
    False
    """
    return contains_3_vowels(str_) and double_letter(str_) and not evil_strings(str_)

if __name__ == "__main__":
    print("Provide puzzle input:")

    strs = []

    try:
        while True:
            strs.append(input())
            
    except KeyboardInterrupt:
        pass

    print("Part 1:")
    strs = [str_ for str_ in strs if nice(str_)]
    print(len(strs))