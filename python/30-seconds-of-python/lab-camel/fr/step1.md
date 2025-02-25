# Chaîne en camelCase

On vous donne une chaîne de caractères qui peut contenir des espaces, des tirets ou des underscores. Votre tâche consiste à convertir la chaîne en camelCase en supprimant les espaces, les tirets ou les underscores et en mettant en majuscule la première lettre de chaque mot, sauf le premier. La première lettre de la chaîne résultante doit être en minuscules.

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
