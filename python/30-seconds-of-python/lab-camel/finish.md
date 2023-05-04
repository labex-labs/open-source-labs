## Summary

In this challenge, you learned how to convert a string to camelcase by removing spaces, hyphens, or underscores and capitalizing the first letter of each word except the first one. You used `re.sub()` to replace any `-` or `_` with a space, using the regexp `r"(_|-)+"`, `str.title()` to capitalize the first letter of each word and convert the rest to lowercase, and `str.replace()` to remove spaces between words.
