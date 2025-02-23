# 文字列が部分文字列で終わるかどうかを確認する関数

与えられた文字列が別の文字列の部分文字列で終わるかどうかを確認するには、次の手順に従います。

1. ターミナル/SSHを開き、コーディングの練習を始めるために`node`と入力します。
2. `for...in`ループと`String.prototype.slice()`を使って、与えられた`word`の各部分文字列を末尾から取得します。
3. `String.prototype.endsWith()`を使って、現在の部分文字列を`text`と照合します。
4. 一致する部分文字列を見つけた場合は返します。そうでない場合は`undefined`を返します。

上記の手順を実装するコードスニペットは次のとおりです。

```js
const endsWithSubstring = (text, word) => {
  for (let i in word) {
    const substr = word.slice(0, i + 1);
    if (text.endsWith(substr)) return substr;
  }
  return undefined;
};
```

次の例で関数をテストできます。

```js
endsWithSubstring("Lorem ipsum dolor sit amet<br /", "<br />"); // '<br /'
```
