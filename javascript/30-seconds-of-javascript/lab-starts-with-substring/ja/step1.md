# 文字列が部分文字列で始まるかどうかを確認する関数

与えられた文字列が別の文字列の部分文字列で始まるかどうかを確認するには、以下の手順に従います。

- ターミナル/SSHを開き、コーディングを練習するために`node`と入力します。
- `for...in`ループと`String.prototype.slice()`メソッドを使って、与えられた`word`の各部分文字列を先頭から取得します。
- `String.prototype.startsWith()`メソッドを使って、現在の部分文字列を`text`と照合します。
- 一致する部分文字列が見つかった場合はそれを返します。それ以外の場合は`undefined`を返します。

これを行うJavaScript関数は次のとおりです。

```js
const startsWithSubstring = (text, word) => {
  for (let i in word) {
    const substr = word.slice(-i - 1);
    if (text.startsWith(substr)) return substr;
  }
  return undefined;
};
```

この関数を次のように呼び出すことができます。

```js
startsWithSubstring("/>Lorem ipsum dolor sit amet", "<br />"); // returns '/>'
```
