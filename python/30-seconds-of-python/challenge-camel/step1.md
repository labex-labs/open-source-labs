# Camelcase String

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

