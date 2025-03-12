#!/bin/bash
grep -E "isinstance\(index, slice\)" ~/project/readrides.py && echo "Success!" || echo "Couldn't find slice handling in the __getitem__ method."
