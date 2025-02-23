# 年の四半期を判定する関数

年の四半期を判定するには、`quarterOfYear()` 関数を使用します。この関数はオプションの `date` 引数を取り、提供された日付が属する四半期と年を含む配列を返します。

この関数を使用するには、ターミナル/SSH を開き、`node` と入力します。次に、次のコードをコピーして貼り付けます。

```js
const quarterOfYear = (date = new Date()) => [
  Math.ceil((date.getMonth() + 1) / 3),
  date.getFullYear()
];
```

`quarterOfYear()` 関数は、次の手順を使用して四半期と年を計算します。

- `Date.prototype.getMonth()` を使用して、範囲 (0, 11) 内の現在の月を取得し、1 を加えて範囲 (1, 12) にマップします。
- `Math.ceil()` を使用して月を 3 で割り、現在の四半期を取得します。
- `Date.prototype.getFullYear()` を使用して、指定された `date` から年を取得します。
- 引数 `date` を省略することで、デフォルトで現在の日付を使用します。

以下は、`quarterOfYear()` 関数の使用例です。

```js
quarterOfYear(new Date("07/10/2018")); // [ 3, 2018 ]
quarterOfYear(); // [ 4, 2020 ]
```
