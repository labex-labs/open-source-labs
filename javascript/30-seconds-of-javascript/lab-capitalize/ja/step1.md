# 文字列の先頭の文字を大文字にする JavaScript 関数

JavaScript で文字列の先頭の文字を大文字にするには、次の関数を使用します。

```js
const capitalize = (str, lowerRest = false) => {
  const [first, ...rest] = str;
  return (
    first.toUpperCase() +
    (lowerRest ? rest.join("").toLowerCase() : rest.join(""))
  );
};
```

この関数は、配列の分解構文と `String.prototype.toUpperCase()` を使って、文字列の先頭の文字を大文字にします。`lowerRest` 引数は省略可能で、文字列の残りを小文字に変換するには `true` に設定できます。

この関数を使用する方法の例を次に示します。

```js
capitalize("fooBar"); // 'FooBar'
capitalize("fooBar", true); // 'Foobar'
```
