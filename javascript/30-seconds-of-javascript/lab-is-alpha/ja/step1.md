# 文字列がアルファベットのみかどうかを確認する関数

文字列がアルファベットのみで構成されているかどうかを確認するには：

- ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
- `RegExp.prototype.test()` を使って、与えられた文字列がアルファベットの正規表現パターンと一致するかどうかを確認します。
- `isAlpha` 関数は文字列引数を取り、文字列がアルファベットのみで構成されている場合は `true` を返し、そうでない場合は `false` を返します。

以下は例です：

```js
const isAlpha = (str) => /^[a-zA-Z]*$/.test(str);
```

```js
isAlpha("sampleInput"); // true
isAlpha("this Will fail"); // false
isAlpha("123"); // false
```
