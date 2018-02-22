''' Here I continue to solve the chellenges from the section Regex and Parsing
TODO 15: "Detect HTML Tags, Attributes and Attribute Values"
'''

from html.parser import HTMLParser



# TODO 15: "Detect HTML Tags, Attributes and Attribute Values"

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)


    def handle_starttag(self, tag, attrs):
        print(tag)
        if len(attrs):
            for attr in attrs:
                print('->', attr[0], '>', attr[1])

    def handle_endtag(self, tag):
        pass

    def handle_startendtag(self, tag, attrs):
        print(tag)
        if len(attrs):
            for attr in attrs:
                # print(f'-> {attr[0]} > {attr[1]}')
                print('->', attr[0], '>', attr[1])


def main():
    html = ''
    for i in range(int(input())):
        html += input().rstrip()
        html += '\n'

    # print(html)
    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()


if __name__ == '__main__':
    main()
