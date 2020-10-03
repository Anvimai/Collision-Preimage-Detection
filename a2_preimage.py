import hashlib  # import library for hashing

import string   # import library for generating a string object containing all possible characters

from random import *    # import library for random generation


def find_preimage(target, n):

    allchar = string.printable  # object containing all possible characters

    dictionary = {}     # dictionary to hold randomly generated string : hash value pairs { string : hash }

    objective = False   # exit clause

    toMatch = target[0:n]   # truncated string to be matched

    while not objective:
        # randomly generate strings and calculate their hash values until a string with a hash value matching the
        # target to the nth byte is found

        password = "".join(choice(allchar) for x in range(randint(20, 20)))

        m = hashlib.sha256()

        m.update(password.encode())

        m = m.digest()

        m = m[0:n]

        dictionary[m] = password

        if toMatch in dictionary:
            objective = True

    # returns the matching string

    return password

