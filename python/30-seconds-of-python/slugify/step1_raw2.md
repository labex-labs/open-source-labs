# String to Slug Challenge

## Introduction
In web development, it is common to have URLs that contain readable words instead of random characters. These readable words are called slugs. Slugs are used to make URLs more user-friendly and easier to remember. In this challenge, you will create a function that converts a string to a URL-friendly slug.

## Problem
Write a function `slugify(s)` that takes a string `s` as an argument and returns a slug. The function should perform the following operations:
1. Convert the string to lowercase and remove any leading or trailing whitespace.
2. Replace all special characters (i.e., any character that is not a letter, digit, whitespace, hyphen, or underscore) with an empty string.
3. Replace all whitespace, hyphens, and underscores with a single hyphen.
4. Remove any leading or trailing hyphens.

## Example
```py
slugify('Hello World!') # 'hello-world'
slugify('  My Example 123  ') # 'my-example-123'
slugify('This is a long sentence with spaces and punctuation!') # 'this-is-a-long-sentence-with-spaces-and-punctuation'
```

## Summary
In this challenge, you learned how to create a function that converts a string to a URL-friendly slug. You used string methods and regular expressions to remove special characters and replace whitespace, hyphens, and underscores with a single hyphen. By completing this challenge, you have gained a better understanding of how to manipulate strings in Python.