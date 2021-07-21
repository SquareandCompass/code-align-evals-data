# [PROMPT]


def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.

    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # [SOLUTION]

    count = 0
    for i in range(0, len(s), 2):
        if s[i] in "AEIOU":
            count = 1
    return count


# [CHECK]
def check(candidate):

    # Check some simple cases
    assert candidate("aBCdEf") == 1
    assert candidate("abcdefg") == 0
    assert candidate("dBBE") == 0
    assert candidate("B") == 0
    assert candidate("U") == 1
    assert candidate("") == 0
    assert candidate("EEEE") == 2

    # Check some edge cases that are easy to work out by hand.
    assert True


if __name__ == "__main__":
    check(count_upper)