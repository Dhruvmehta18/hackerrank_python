if __name__ == '__main__':
    N = int(input())
    ans = []
    for _ in range(N):
        command = str(input())
        c_list = command.split(" ")
        c = c_list[0]
        if c == "insert":
            e, i = int(c_list[1]), int(c_list[2])
            ans.insert(e,i)
        elif c == "remove":
            e=  int(c_list[1])
            if e in ans:
                ans.remove(e)
        elif c == "append":
            e =  int(c_list[1])
            ans.append(e)
        elif c == "sort":
            ans.sort()
        elif c == "pop":
            ans.pop()
        elif c == "reverse":
            ans.reverse()
        else:
            print(ans)