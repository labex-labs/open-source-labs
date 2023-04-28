# Integer to Roman Numeral Challenge

## Problem
Write a function `to_roman_numeral(num)` that takes an integer `num` between 1 and 3999 (inclusive) and returns its Roman numeral representation as a string.

To convert an integer to its Roman numeral representation, you can use a lookup list containing tuples in the form of (roman value, integer). You can then use a `for` loop to iterate over the values in the lookup list and use `divmod()` to update `num` with the remainder, adding the Roman numeral representation to the result.

Your function should return the Roman numeral representation of the input integer.

## Example
```py
to_roman_numeral(3) # 'III'
to_roman_numeral(11) # 'XI'
to_roman_numeral(1998) # 'MCMXCVIII'
```

