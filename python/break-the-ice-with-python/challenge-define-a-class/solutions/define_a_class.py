class IOstring:
    def __init__(self):
        self.s = ""

    def get_string(self):
        self.s = input()

    def print_string(self):
        print(self.s.upper())


xx = IOstring()
xx.get_string()
xx.print_string()
