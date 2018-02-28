''' Here I continue to solve the chellenges by HackerRank
TODO 2 "Decorators 2 - Name Directory"
Let's use decorators to build a name directory! You are given some information about  people. Each person has a first name, last name, age and sex. Print their names in a specific format sorted by their age in ascending order i.e. the youngest person's name should be printed first. For two people of the same age, print them in the order of their input.
For Henry Davids, the output should be: Mr. Henry Davids
For Mary George, the output should be: Ms. Mary George

'''

import operator

def to_int(person):
    person[2] = int(person[2])
    return person

def person_lister(f):
    def inner(people):
        # complete the function
        people = list(map(to_int, people))
        # print('people before sort =', people)
        people.sort(key=operator.itemgetter(2))
        # print('people after sort =', people)
        # people = sorted(people, key=operator.itemgetter(2))
        # print('people after sort =', people)
        print()
        new_l = []
        new_person = ''
        for person in people:
            # new_person = 'Mr. ' if person[3] == 'M' else 'Ms. '
            # new_person += person[0] + ' ' + person[1]
            new_person = ' '.join(['Mr.' if person[3] == 'M' else 'Ms.', person[0], person[1], str(person[2])])
            new_l.append(new_person)
            # new_l.append(f(person))
        # print('new_l =', new_l)
        return new_l

    return inner


@person_lister
def name_format(person):
    # return('Mr. ' if person[3] == 'M' else 'Ms. ' + person[0] + ' ' + person[1])
    return(' '.join(['Mr. ' if person[3] == 'M' else 'Ms. ', person[0], person[1]]))


if __name__ == "__main__":
    people = [input().split() for i in range(int(input()))]
    # print(people)
    # print(people.sort(key=operator.itemgetter(2)))
    # print(people)

    print(*name_format(people), sep='\n')
