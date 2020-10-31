import random, string
v_pool = "aeiouy"
c_pool = ["bcdfghjklmnpqrstvwxz", "adfasd","sdfs","dfddd"]
l_pool = string.ascii_lowercase
def generateCharactor(opt):
    if "v" == opt:
        return random.choice(v_pool)
    elif "c" == opt:
        return random.choice(c_pool)
    elif "l" == opt:
        return random.choice(l_pool)
    else:
        return opt

opt1 = input("1st char please select: 'v' for vowels, 'c' for consonants, 'l' for any letters: ")
opt2 = input("2nd char please select: 'v' for vowels, 'c' for consonants, 'l' for any letters: ")
opt3 = input("3rd char please select: 'v' for vowels, 'c' for consonants, 'l' for any letters: ")

for i in range(20):
    print(generateCharactor(opt1)+generateCharactor(opt2)+generateCharactor(opt3))
