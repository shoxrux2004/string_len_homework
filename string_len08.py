from math import*
def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    n=ceil(len(s)/2)
    if(len(s)%2==1):
        return s[n-1]
    else:
        return s[n]+s[n-1]
print(main("abcdf"))
print(main("cool"))