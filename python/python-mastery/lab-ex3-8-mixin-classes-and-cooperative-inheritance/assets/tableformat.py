# tableformat.py
from abc import ABC, abstractmethod


def print_table(records, fields, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError("Expected a TableFormatter")

    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)


class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(" ".join("%10s" % h for h in headers))
        print(("-" * 10 + " ") * len(headers))

    def row(self, rowdata):
        print(" ".join("%10s" % d for d in rowdata))


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(",".join(headers))

    def row(self, rowdata):
        print(",".join(str(d) for d in rowdata))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print("<tr>", end=" ")
        for h in headers:
            print("<th>%s</th>" % h, end=" ")
        print("</tr>")

    def row(self, rowdata):
        print("<tr>", end=" ")
        for d in rowdata:
            print("<td>%s</td>" % d, end=" ")
        print("</tr>")


# ------------------------------------------------------------------------------------------ #
# Do step 2 here


class ColumnFormatMixin:
    pass


class UpperHeadersMixin:
    pass


# ------------------------------------------------------------------------------------------ #


def create_formatter(name, column_formats=None, upper_headers=False):
    if name == "text":
        formatter_cls = TextTableFormatter
    elif name == "csv":
        formatter_cls = CSVTableFormatter
    elif name == "html":
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError("Unknown format %s" % name)
    # ------------------------------------------------------------------------------------------ #
    # Do step 3 here

    pass
    # ------------------------------------------------------------------------------------------ #

    return formatter_cls()
