# Integer to Roman Numeral Challenge

## Introduction
Roman numerals are a numeral system that originated in ancient Rome. They are still used today in various contexts, such as in the numbering of book chapters and movie sequels. In this challenge, you will be tasked with creating a function that converts an integer between 1 and 3999 (inclusive) to its Roman numeral representation.

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

## Summary
In this challenge, you learned how to convert an integer to its Roman numeral representation. You used a lookup list containing tuples in the form of (roman value, integer) and a `for` loop to iterate over the values in the lookup list. You also used `divmod()` to update `num` with the remainder, adding the Roman numeral representation to the result.