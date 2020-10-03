def hammingdistance(hex1, hex2):
    dif = 0  # counter for the hamming distance between hex values

    number = ("{0:b}".format(int(hex1.rstrip("\n"), 16)))  # binary representation of hex1

    number2 = ("{0:b}".format(int(hex2.rstrip("\n"), 16)))  # binary representation of hex2

    # Loop through each binary string comparing characters
    # Counting each character that does not match
    # ensure strings with different lengths are handled appropriately
    if len(number) > len(number2):
        dif += len(number) - len(number2) - 1
        index = 0
        for i in number2:
            if i != number[index]:
                dif += 1
            index += 1
    else:
        dif += len(number2) - len(number)
        index = 0
        for i in number:
            if i != number2[index]:
                dif += 1
            index += 1

    # returns the total hamming distance between strings 
    return dif
