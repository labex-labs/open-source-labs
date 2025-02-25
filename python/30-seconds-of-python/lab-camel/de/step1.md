# Camelcase-String

Es wird Ihnen ein String gegeben, der möglicherweise Leerzeichen, Bindestriche oder Unterstriche enthält. Ihre Aufgabe besteht darin, den String in Camelcase umzuwandeln, indem Sie die Leerzeichen, Bindestriche oder Unterstriche entfernen und den ersten Buchstaben jedes Wortes außer dem ersten in Großbuchstaben setzen. Der erste Buchstabe des resultierenden Strings sollte in Kleinbuchstaben sein.

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
