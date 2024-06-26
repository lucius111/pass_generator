import random


def gen_pass(length):
    charGroups = [
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'abcdefghijklmnopqrstuvwxyz',
        '0123456789',
        '~!@#$%^&*()-_=+[{]}\|;:\'",<.>/?'
    ]

    res = ''
    got = set()
    while len(res) < length:
        group = random.randint(0, len(charGroups)-1)

        got.add(group)
        res += charGroups[group][random.randint(0, len(charGroups[group])-1)]

    return res