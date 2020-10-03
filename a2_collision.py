import hashlib  # import library for hashing

import string  # import library for generating a string object containing all possible characters

from random import *  # import library for random generation


def find_collision(n):
    allchar = string.printable  # object containing all possible characters

    dictionary = {}  # dictionary to hold randomly generated string : hash value pairs { string : hash }

    objective = False  # exit clause

    while not objective:
        # randomly generate strings and calculate their hash values until two distinct strings
        # have the same hash value to the nth byte

        password1 = "".join(choice(allchar) for x in range(randint(20, 20)))

        m1 = hashlib.sha256()
        m1.update(password1.encode())
        m1 = m1.digest()
        m1 = m1[0:n]

        if m1 in dictionary:
            objective = True
            ans = (password1, dictionary[m1])

        else:
            dictionary[m1] = password1

    # returns a tuple containing the two distinct strings that hash values collide to the nth byte

    return ans
