from Securities import *
from termcolor import colored

class Format:
    def __init__(self, holdings):
        self.stocks = []
        self.crypto = []
        self.cash = []

        self.tot_val = 0.0
        self.in_val = 0.0

        for elem in holdings:
            if elem.get_type() == 'crypto':
                self.tot_val += elem.get_cur_val()
                self.in_val += elem.get_in_val()
                self.crypto.append(elem)
            elif elem.get_type() == 'stock':
                self.tot_val += elem.get_cur_val()
                self.in_val += elem.get_in_val()
                self.stocks.append(elem)
            else:
                self.tot_val += elem.get_cur_val()
                self.in_val += elem.get_in_val()
                self.cash.append(elem)

        self.total = Securities('TOTAL', 'total', 1, self.in_val, self.tot_val)

    def print(self):
        output = ""
        output += "PORTFOLIO: \n"
        output += '\nSTOCKS\n' + '---------\n'
        for elem in self.stocks:
            output += self.build_str(elem)

        output += '\n'
        output += "\nCRYPTO\n" + '---------\n'
        for elem in self.crypto:
            output += self.build_str(elem)

        output += '\n'
        output += "\nCASH\n" + '---------\n'
        for elem in self.cash:
            output += self.build_str(elem)

        output += '\n\n'
        output += self.build_end(self.total)

        print(output)


    def build_str(self, elem):
        output = ""
        output += elem.get_name() + " | Current Value: "
        cur_val = elem.get_cur_val()
        output += str("{:.2f}".format(cur_val)) + " | Current Price: "
        cur_price = elem.get_cur_price()
        output += "{:.2f}".format(float(cur_price))
        output += "\n\tInitial Value: "
        output += str(elem.get_in_val()) + " | Initial Price: " + str(elem.get_in_price())

        growth = elem.get_perc_growth()
        output += " | Change: "
        output += colored(str("{:.2f}".format(growth)) + " %", 'green') if growth > 0.0 else \
            colored(str("{:.2f}".format(growth)) + " %", 'red')
        output += "\n"

        return output


    def build_end(self, elem):
        output = ""
        output += elem.get_name() + " | Current Value: "
        cur_val = elem.get_cur_val()
        output += str("{:.2f}".format(cur_val))
        output += " | Initial Value: "
        output += str(elem.get_in_val())
        growth = elem.get_perc_growth()
        output += " | Change: "
        output += colored(str("{:.2f}".format(growth)) + " %", 'green') if growth > 0.0 else \
            colored(str("{:.2f}".format(growth)) + " %", 'red')
        output += "\n"

        return output
