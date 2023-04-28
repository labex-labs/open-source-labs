# Snakecase String

## Introduction
In Python, snake case is a naming convention where words are separated by underscores. This is commonly used for naming variables, functions, and other identifiers. However, sometimes we may have strings that are not in snake case and we need to convert them. In this challenge, you will be tasked with writing a Python function that converts a string to snake case.

## Problem
Write a Python function called `snake` that takes a string as its argument and returns the string in snake case. The function should perform the following steps:
1. Use `re.sub()` to match all words in the string, `str.lower()` to lowercase them.
2. Use `re.sub()` to replace any `-` characters with spaces.
3. Finally, use `str.join()` to combine all words using `_` as the separator.

Your function should be able to handle strings with a mix of uppercase and lowercase letters, spaces, hyphens, and underscores.

## Example
```py
snake('camelCase') # 'camel_case'
snake('some text') # 'some_text'
snake('some-mixed_string With spaces_underscores-and-hyphens')
# 'some_mixed_string_with_spaces_underscores_and_hyphens'
snake('AllThe-small Things') # 'all_the_small_things'
```

## Summary
In this challenge, you learned how to write a Python function that converts a string to snake case. You used `re.sub()` to match and replace words in the string, `str.lower()` to lowercase them, and `str.join()` to combine them using underscores as the separator. With this knowledge, you can now easily convert strings to snake case in your Python programs.