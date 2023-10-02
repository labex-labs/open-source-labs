import sys

sys.path.append('/home/labex/project')

import report
from tableformat import create_formatter, print_table

def test_print_table():
    
    portfolio = report.read_portfolio('portfolio.csv') 
    formatter = create_formatter('txt')
    expected_output_1 = "price"

    import sys
    from io import StringIO
    captured_output = StringIO()
    sys.stdout = captured_output

    print_table(portfolio, ['name', 'shares'], formatter)
    output = captured_output.getvalue()
 
    sys.stdout = sys.__stdout__

    assert expected_output_1 not in output

    print("All assertions passed.")

if __name__ == '__main__':
    test_print_table()