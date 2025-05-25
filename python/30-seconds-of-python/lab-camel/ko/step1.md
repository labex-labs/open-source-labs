# Camelcase 문자열

공백, 하이픈 또는 밑줄을 포함할 수 있는 문자열이 주어집니다. 당신의 과제는 공백, 하이픈 또는 밑줄을 제거하고 첫 번째 단어를 제외한 각 단어의 첫 글자를 대문자로 변환하여 문자열을 camelcase 로 변환하는 것입니다. 결과 문자열의 첫 글자는 소문자여야 합니다.

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
