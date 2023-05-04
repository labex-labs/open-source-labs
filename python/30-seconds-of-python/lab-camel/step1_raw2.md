# Camelcase String

## Introduction

Camelcase is a naming convention where a compound word or phrase is written in a way that the first word is in lowercase and the subsequent words are capitalized. This naming convention is commonly used in programming languages to name variables, functions, and classes.

## Problem

You are given a string that may contain spaces, hyphens, or underscores. Your task is to convert the string to camelcase by removing the spaces, hyphens, or underscores and capitalizing the first letter of each word except the first one. The first letter of the resulting string should be in lowercase.

## Example

```py
camel('some_database_field_name') # 'someDatabaseFieldName'
camel('Some label that needs to be camelized')
# 'someLabelThatNeedsToBeCamelized'
camel('some-javascript-property') # 'someJavascriptProperty'
camel('some-mixed_string with spaces_underscores-and-hyphens')
# 'someMixedStringWithSpacesUnderscoresAndHyphens'
```

## Summary

In this challenge, you learned how to convert a string to camelcase by removing spaces, hyphens, or underscores and capitalizing the first letter of each word except the first one. You used `re.sub()` to replace any `-` or `_` with a space, using the regexp `r"(_|-)+"`, `str.title()` to capitalize the first letter of each word and convert the rest to lowercase, and `str.replace()` to remove spaces between words.
