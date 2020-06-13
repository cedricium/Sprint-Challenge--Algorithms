def count_th(word):
    if len(word) < 2:
        return 0
    if word[:2] == 'th':
        return 1 + count_th(word[2:])
    return 0 + count_th(word[1:])
