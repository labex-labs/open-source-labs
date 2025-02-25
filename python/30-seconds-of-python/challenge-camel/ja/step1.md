# キャメルケース文字列

## 問題

空白、ハイフン、またはアンダースコアを含む文字列が与えられます。あなたのタスクは、空白、ハイフン、またはアンダースコアを削除し、最初の単語以外の各単語の最初の文字を大文字にすることで、文字列をキャメルケースに変換することです。結果の文字列の最初の文字は小文字でなければなりません。

## 例

```python
camel('some_database_field_name') # 'someDatabaseFieldName'
camel('Some label that needs to be camelized')
# 'someLabelThatNeedsToBeCamelized'
camel('some-javascript-property') # 'someJavascriptProperty'
camel('some-mixed_string with spaces_underscores-and-hyphens')
# 'someMixedStringWithSpacesUnderscoresAndHyphens'
```
