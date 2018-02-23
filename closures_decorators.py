''' Here I continue to solve the chellenges by HackerRank
TODO 1 "Standardize Mobile Number Using Decorators"
'''


def clear_phone(str):
    str = str[len(str)-10:]
    new_str = '+91 ' + str[0:5] + ' ' + str[5:]
    return new_str

def wrapper(f):
    def fun(l):
        # complete the function
        new_l = []
        for s in l:
            new_l.append(clear_phone(s))
        return f(new_l)
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == "__main__":
    l = [input() for _ in range(int(input()))]

    sort_phone(l)


