''' Here I continue to solve the chellenges from the section Regex and Parsing
TODO 13: "HTML Parser - Part 1"
'''

# import sys
# from HTMLParser import HTMLParser
from html.parser import HTMLParser



# TODO 13: "HTML Parser - Part 1"

# create a subclass and override the handler methods
# For instance, for the tag <A HREF="https://www.cwi.nl/">, this method would be called as
# handle_starttag('a', [('href', 'https://www.cwi.nl/')]).
class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []  #  список найденных ссылок
        self.start_tag_list = []
        self.end_tag_list = []
        self.empty_tag_list = []
        self.out_data = []

    def handle_starttag(self, tag, attrs):
        ''' Переопределяем метод HTMLParser (в базовом классе метод ничего не делает)
        Сам метод вызывается для обработки начала тега (фактически вызывается для каждого
        начального тега при вызове метода "feed").
        '''
        # attrs = dict(attrs)
        # # если находим тег 'a'
        # if 'a' == tag:
        #     try:
        #         # print attrs['href']
        #         # записываем значение аттрибута href в список-свойство links нашего класса
        #         self.links.append(attrs['href'])
        #     except:
        #         pass
        # for i in self.links:
        #     print(i)
        # print(f"Found a start tag  :{tag}")

        # print("Found a start tag  :", tag)
        self.out_data.append(f"Start :{tag}")
        # print("Start :", tag)
        if len(attrs):
            for attr in attrs:
                # print(f'-> {attr[0]} > {attr[1]}')
                self.out_data.append(f'-> {attr[0]} > {attr[1]}')
                # print('->', attr[0], '>', attr[1])

    def handle_endtag(self, tag):
        # print("End   :", tag)
        self.out_data.append(f"End   :{tag}")

    def handle_startendtag(self, tag, attrs):
        self.out_data.append(f"Empty :{tag}")
        # print("Empty :", tag)
        if len(attrs):
            for attr in attrs:
                # print(f'-> {attr[0]} > {attr[1]}')
                self.out_data.append(f'-> {attr[0]} > {attr[1]}')
                # print('->', attr[0], '>', attr[1])


def main():
    # mod_divmod()
    inp_str = ''
    n = int(input())
    for _ in range(n):
        # inp_str = input().lstrip().rstrip()
        inp_str += input()
        # inp_str = stdin.readline().lstrip().rstrip().strip()
        # print(inp_str)
    # instantiate the parser and fed it some HTML
    parser = MyHTMLParser()
    # parser.feed("<html><head><title>HTML Parser - I</title></head>"
    #             + "<body><h1>HackerRank</h1><br /></body></html>")
    parser.feed(inp_str)
    for str in parser.out_data:
        print(str)



if __name__ == '__main__':
    main()
