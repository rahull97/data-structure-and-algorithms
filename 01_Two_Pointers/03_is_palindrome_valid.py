def is_palindrome_valid(s: str) -> bool:
    left = 0
    right = len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left = left + 1
        elif not s[right].isalnum():
            right = right - 1
        elif s[left].isalnum() and s[right].isalnum():
            if s[left] == s[right]:
                left = left + 1
                right = right - 1
            else:
                return False
    return True


if __name__ == "__main__":
    print(is_palindrome_valid(""))
    print(is_palindrome_valid("a"))
    print(is_palindrome_valid("aa"))
    print(is_palindrome_valid("ab"))
    print(is_palindrome_valid("!, (?)"))
    print(is_palindrome_valid("12.02.2021"))
    print(is_palindrome_valid("21.02.2021"))
    print(is_palindrome_valid("hello, world!"))
    print(is_palindrome_valid("a dog! a panic in a pagoda."))
    print(is_palindrome_valid("abc123"))
