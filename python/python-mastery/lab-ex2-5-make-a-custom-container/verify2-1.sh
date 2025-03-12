#!/bin/bash
grep -E "row\[" ~/.python_history && echo "Success!" || echo "Couldn't find evidence of dictionary operations in your Python history."
