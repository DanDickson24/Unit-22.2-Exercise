def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    num_counts = {}
    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1

    # find the number with the highest frequency
    max_count = 0
    mode_num = None
    for num, count in num_counts.items():
        if count > max_count:
            max_count = count
            mode_num = num

    return mode_num
