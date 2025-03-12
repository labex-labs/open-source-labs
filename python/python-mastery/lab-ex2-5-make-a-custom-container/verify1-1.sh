#!/bin/bash
grep -E "sys\.getsizeof|append" ~/.python_history && echo "Success!" || echo "Couldn't find evidence of using sys.getsizeof() and append() in your Python history."
