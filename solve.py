import argparse
import enchant
import itertools


D = enchant.Dict("en_US")


def permute(word):
    words = []
    for i in range(3, 10):
        if len(word) > 10:
            pass
        else:
            permuations = itertools.permutations(word, i)
            permuations = set(''.join(p) for p in permuations)
            for permuation in permuations:
                if D.check(permuation):
                    words.append(permuation)
    return words

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('word')
    args = parser.parse_args()
    word = args.word
    possibilites = permute(word)
    possibilites.sort()
    possibilites.sort(key=len)
    for possibility in possibilites:
        print(possibility)
