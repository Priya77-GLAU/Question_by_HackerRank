''' Python question by HackerRank
TODO 1:
"collections.Counter()"
Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay X amount of money only if they get the shoe of their desired size.
Your task is to compute how much money Raghu earned.
Input Format
The first line contains X, the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains N, the number of customers.
The next N lines contain the space separated values of the  desired by the customer and , the price of the shoe.
Constraints
0 < X < 10**3
0 < N <= 10**3
20 < x_i < 100
2 < shoe_size < 20
Output Format: Print the amount of money earned by Raghu .

TODO 2:
"DefaultDict Tutorial"

'''

from collections import Counter
from collections import defaultdict


# TODO 1: "collections.Counter()"
def get_size_and_price():
    input_list = input().lstrip().rstrip().split(' ')
    return int(input_list[0]), int(input_list[1])


def collections_counter():
    num_of_shoes = int(input())
    shoe_size_list = Counter([int(x) for x in input().lstrip().rstrip().split(' ')])
    num_of_customers = int(input())
    money = 0
    for i in range(num_of_customers):
        size, price = get_size_and_price()
        if shoe_size_list[size] > 0:  # size in shoe_size_list
            shoe_size_list[size] -= 1
            money += price
    print(money)


# TODO 2: "DefaultDict Tutorial"
def default_dict_tutorial():
    n, m = [int(x) for x in input().lstrip().rstrip().split(' ')]
    group_a = []
    for i in range(n):
        group_a.append(input().lstrip().rstrip())

    for word_i in range(m):
        word_group_b = input().lstrip().rstrip()
        if word_group_b in group_a:  # len([x for x in group_a if x == word_group_b])
            for i, ch in enumerate(group_a, 1):
                if ch == word_group_b:
                    print(i, end=' ')
                else:
                    pass
            print()
        else:
            print('-1')

            # result = defaultdict(list)
            # for word_i in range(m):
            #     word_group_b = input().lstrip().rstrip()
            #     if word_group_b in group_a:
            #         for i,ch  in enumerate(group_a, 1):
            #             if ch == word_group_b:
            #                 result[word_group_b].append(i)
            #             else:
            #                 pass
            #     else:
            #         result[word_group_b].append('-1')
            #     print(result)


def main():
    # collections_counter()
    default_dict_tutorial()


if __name__ == '__main__':
    main()
