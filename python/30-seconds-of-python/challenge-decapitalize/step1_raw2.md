# Decapitalize String

## Introduction
In Python, strings are immutable, meaning that they cannot be changed once they are created. However, there are times when we need to modify a string, such as when we want to decapitalize the first letter. This can be useful when dealing with user input or when formatting strings for display purposes. In this challenge, you will be tasked with writing a function that decapitalizes the first letter of a string.

## Problem
Write a function `decapitalize(s, upper_rest = False)` that takes a string `s` and returns a new string with the first letter decapitalized. The function should also have an optional parameter `upper_rest` that, when set to `True`, will convert the rest of the string to uppercase.

## Example
```py
decapitalize('FooBar') # 'fooBar'
decapitalize('FooBar', True) # 'fOOBAR'
```

## Summary
In this challenge, you learned how to decapitalize the first letter of a string in Python. You used list slicing and `str.lower()` to decapitalize the first letter of the string, and `str.join()` to combine the lowercase first letter with the rest of the characters. You also learned how to use an optional parameter to convert the rest of the string to uppercase.