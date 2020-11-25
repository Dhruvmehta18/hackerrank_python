def min_by_score(sequence):
    if not sequence:
        raise ValueError('empty sequence')

    minimum = sequence[0]
    minimum2 = None
    for item in sequence[1:]:
        if item[1] != minimum[1]:
            if item[1] < minimum[1]:
                minimum2 = minimum[1]
                minimum = item
            elif minimum2 is None or minimum2 > item[1]:  
                minimum2 = item[1]
    return minimum2

if __name__ == '__main__':
    l = [[input(),float(input())] for _ in range(int(input()))]
    sl = sorted(l)
    m = min_by_score(sl)
    print('\n'.join([i[0] for i in sl if i[1]==m]))