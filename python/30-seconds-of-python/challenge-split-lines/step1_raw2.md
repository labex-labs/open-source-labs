# Split into Lines

## Introduction
In Python, a multiline string is a string that contains multiple lines of text. Sometimes, it is necessary to split a multiline string into a list of individual lines. This can be useful when you need to process each line separately.

## Problem
Write a function called `split_lines(s)` that takes a multiline string `s` as input and returns a list of individual lines. Your function should split the string at each line break (`\n`) and return a list of the resulting lines.

## Example
```py
split_lines('This\nis a\nmultiline\nstring.\n')
# ['This', 'is a', 'multiline', 'string.' , '']
```

## Summary
To split a multiline string into a list of individual lines in Python, you can use the `split()` method with the line break character (`\n`) as the delimiter. This will split the string at each line break and return a list of the resulting lines.