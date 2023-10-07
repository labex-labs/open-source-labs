import sys

sys.path.append('/home/labex/project')

from tableformat import create_formatter, FormatError

def test_create_formatter_with_unknown_format():
    try:
        formatter = create_formatter('xls')
        assert False, "FormatError was not raised"
    except FormatError as e:
        assert str(e) == "Unknown table format xls"

if __name__ == '__main__':
    test_create_formatter_with_unknown_format()
    print("All assertions passed.")