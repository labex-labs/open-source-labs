# String em Camelcase

É fornecida uma string que pode conter espaços, hífens ou underscores. Sua tarefa é converter a string para camelcase removendo os espaços, hífens ou underscores e capitalizando a primeira letra de cada palavra, exceto a primeira. A primeira letra da string resultante deve estar em minúsculas.

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
