# 驼峰式字符串

## 问题

你会得到一个可能包含空格、连字符或下划线的字符串。你的任务是通过移除空格、连字符或下划线，并将除第一个单词外的每个单词的首字母大写，将该字符串转换为驼峰式。结果字符串的首字母应该是小写。

## 示例

```python
camel('some_database_field_name') # 'someDatabaseFieldName'
camel('Some label that needs to be camelized')
# 'someLabelThatNeedsToBeCamelized'
camel('some-javascript-property') # 'someJavascriptProperty'
camel('some-mixed_string with spaces_underscores-and-hyphens')
# 'someMixedStringWithSpacesUnderscoresAndHyphens'
```
