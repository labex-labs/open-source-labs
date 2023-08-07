# Step 2 Solution

# ------------------------------------------------------------------------------------------ #
# The solution is here
def print_table(records, fields, formatter):
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)


class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()

# ------------------------------------------------------------------------------------------ #
