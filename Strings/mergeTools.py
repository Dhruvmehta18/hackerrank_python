def merge_the_tools(string, k):
    for parts in zip(*[iter(string)]*k):
        d = dict()
        print(''.join([d.setdefault(part, part) for part in parts if part not in d ]))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)