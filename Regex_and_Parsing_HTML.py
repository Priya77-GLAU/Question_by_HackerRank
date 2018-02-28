''' Here I continue to solve the chellenges by HackerRank
TODO "Time Delta"
'''

#import sys

def time_delta(t1, t2):
    print(t1, 'vs', t2)
    # Complete this function

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        t1 = input().strip()
        t2 = input().strip()
        delta = time_delta(t1, t2)
        print(delta)