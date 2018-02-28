''' Here I continue to solve the chellenges from the section Regex and Parsing
TODO 14: "HTML Parser - Part 2"
'''

from html.parser import HTMLParser


# TODO 13: "HTML Parser - Part 1"
class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        #  список найденных ссылок
        self.links = []
        self.start_tag_list = []
        self.end_tag_list = []
        self.empty_tag_list = []
        self.out_data = []

    def handle_comment(self, data):
        data_list = data.split('\n')
        if len(data_list) > 1:
            print('>>> Multi-line Comment')
        else:
            print(">>> Single-line Comment")

        print(data)

    def handle_data(self, data):
        if len(data) > 2:
            print(">>> Data")
            print(data)
            # print(type(data))
            # print('len data: ', len(data))


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
