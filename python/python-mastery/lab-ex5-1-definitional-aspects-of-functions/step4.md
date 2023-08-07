# Design Challenge: CSV Headers

The code assumes that the first line of CSV data always contains
column headers. However, this isn't always the case. For example, the
file `portfolio_noheader.csv` contains data, but no column
headers.

How would you refactor the code to accommodate missing column headers, having
them supplied manually by the caller instead?
