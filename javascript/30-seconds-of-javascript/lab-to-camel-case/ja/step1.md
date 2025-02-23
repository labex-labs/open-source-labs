# キャメルケース文字列変換

文字列をキャメルケースに変換するには、次の手順に従います。

1. ターミナル/SSHを開き、コーディングの練習を始めるために `node` と入力します。
2. 適切な正規表現を使って `String.prototype.match()` を使って文字列を単語に分割します。
3. `Array.prototype.map()`, `Array.prototype.slice()`, `Array.prototype.join()`, `String.prototype.toLowerCase()`、および `String.prototype.toUpperCase()` を使って単語を結合し、各単語の先頭文字を大文字にします。
4. 以下に示す `toCamelCase` 関数を使って変換を行います。

```js
const toCamelCase = (str) => {
  const words =
    str &&
    str.match(
      /[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g
    );
  const capitalizedWords =
    words &&
    words.map(
      (word) => word.slice(0, 1).toUpperCase() + word.slice(1).toLowerCase()
    );
  const camelCaseString = capitalizedWords && capitalizedWords.join("");
  return (
    camelCaseString &&
    camelCaseString.slice(0, 1).toLowerCase() + camelCaseString.slice(1)
  );
};
```

以下は、`toCamelCase` 関数の使い方のいくつかの例です。

```js
toCamelCase("some_database_field_name"); //'someDatabaseFieldName'
toCamelCase("Some label that needs to be camelized");
//'someLabelThatNeedsToBeCamelized'
toCamelCase("some-javascript-property"); //'someJavascriptProperty'
toCamelCase("some-mixed_string with spaces_underscores-and-hyphens");
//'someMixedStringWithSpacesUnderscoresAndHyphens'
```
