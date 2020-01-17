from cs50 import get_string
from sys import argv, exit


def main():
    if len(argv) != 2:
        exit(1)
    file = open(argv[1], 'r')
    banned = file.readlines()
    i = 0
    for word in banned:
        banned[i] = word.strip()
        i += 1
    message = get_string("message: ")
    splitMes = message.split()
    joinMes = []
    for word in splitMes:
        if word.lower() in banned:
            new = list(word)
            for c in range(len(word)):
                new[c] = '*'
            new = ''.join(new)
            joinMes.append(new)
        else:
            joinMes.append(word)
    newMes = ' '.join(joinMes)
    print(newMes)

if __name__ == "__main__":
    main()