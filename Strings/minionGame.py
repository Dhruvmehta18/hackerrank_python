def minion_game(string):
    vowel = ['A', 'E','I','O','U']
    s = 0
    k = 0
    for i in range(len(string)):
        if string[i] in vowel:
            k += len(string) - i
        else:
            s += len(string) - i
    if s>k:
        print("Stuart", s)
    elif k>s:
        print("Kevin", k)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)