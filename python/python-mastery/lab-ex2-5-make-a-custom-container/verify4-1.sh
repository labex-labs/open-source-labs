#!/bin/bash
grep -E "class RideData|__len__|__getitem__" ~/project/readrides.py && echo "Success!" || echo "Couldn't find the RideData class with required methods in readrides.py."
