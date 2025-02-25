# Строка в camelCase

Вам дается строка, которая может содержать пробелы, дефисы или подчеркивания. Ваша задача - преобразовать строку в camelCase, удалив пробелы, дефисы или подчеркивания и сделав заглавной первую букву каждого слова, кроме первого. Первая буква результирующей строки должна быть в нижнем регистре.

```python
from re import sub

def camel(s):
  s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
  return ''.join([s[0].lower(), s[1:]])
```

```python
camel('some_database_field_name') # 'someDatabaseFieldName'
camel('Some label that needs to be camelized')
# 'someLabelThatNeedsToBeCamelized'
camel('some-javascript-property') # 'someJavascriptProperty'
camel('some-mixed_string with spaces_underscores-and-hyphens')
# 'someMixedStringWithSpacesUnderscoresAndHyphens'
```
