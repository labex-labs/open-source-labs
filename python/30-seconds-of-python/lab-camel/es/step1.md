# Cadena en camelCase

Se te da una cadena que puede contener espacios, guiones o subrayados. Tu tarea es convertir la cadena a camelCase eliminando los espacios, guiones o subrayados y capitalizando la primera letra de cada palabra excepto la primera. La primera letra de la cadena resultante debe estar en minúsculas.

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
