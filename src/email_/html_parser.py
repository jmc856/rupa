from html.parser import HTMLParser as HTMLParser_


class HTMLParser(HTMLParser_):
    """
    Extend Python built in html parser to convert html -> plaintext
    """

    def __init__(self):
        super().__init__()
        self.plaintext = ""

    def parse(self, data):
        self.feed(data)
        plaintext = self.plaintext
        self.plaintext = ""
        return plaintext

    def handle_data(self, data):
        """
        Overrides HTMLParser method that captures all non tagged text
        """

        if self.plaintext == '':
            self.plaintext += data
        else:
            self.plaintext += f' {data}'
