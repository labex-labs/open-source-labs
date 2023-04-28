# Kebabcase string

## Introduction

In Python, a kebab case string is a string where each word is separated by a hyphen. For example, "hello-world" is a kebab case string. In this challenge, you will be tasked with writing a function that converts a given string to kebab case.

## Problem

Write a Python function called `to_kebab_case(s)` that takes a string `s` as its input and returns the kebab case version of the string. The function should perform the following steps:

1. Replace any `-` or `_` with a space, using the regexp `r"(_|-)+"`.
2. Match all words in the string, `str.lower()` to lowercase them.
3. Combine all words using `-` as the separator.

## Example

```py
to_kebab_case('camelCase') # 'camel-case'
to_kebab_case('some text') # 'some-text'
to_kebab_case('some-mixed_string With spaces_underscores-and-hyphens')
# 'some-mixed-string-with-spaces-underscores-and-hyphens'
to_kebab_case('AllThe-small Things') # 'all-the-small-things'
```

## Summary

In this challenge, you learned how to convert a string to kebab case in Python. You used `re.sub()` to replace any `-` or `_` with a space, `re.sub()` to match all words in the string, `str.lower()` to lowercase them, and `str.join()` to combine all words using `-` as the separator.
