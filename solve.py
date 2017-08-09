import argparse
import enchant
import itertools


D = enchant.Dict("en_US")


def permute(word):
    words = set()
    for i in range(3, 10):
        ps = itertools.permutations(word, i)
        permuations = [''.join(p) for p in ps]
        for permuation in permuations:
            if D.check(permuation):
                words.add(permuation)
    return list(words)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('word')
    args = parser.parse_args()
    word = args.word
    possibilities = permute(word)
    possibilities.sort()
    possibilities.sort(key=len)
    for possibility in possibilities:
        print(possibility)
