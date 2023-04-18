def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """
    # Convert the numbers to strings
    str1 = str(num1)
    str2 = str(num2)

    # If the lengths of the strings are different, they can't have the same frequency of digits
    if len(str1) != len(str2):
        return False

    # Create dictionaries to count the frequencies of digits in the numbers
    freq1 = {}
    freq2 = {}

    for char in str1:
        freq1[char] = freq1.get(char, 0) + 1

    for char in str2:
        freq2[char] = freq2.get(char, 0) + 1

    # Check if the frequency dictionaries are the same
    return freq1 == freq2
