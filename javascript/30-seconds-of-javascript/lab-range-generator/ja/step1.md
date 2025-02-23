# 範囲生成器

指定されたステップを使って値の範囲を生成するには、次の `rangeGenerator` 関数を使用します。ターミナル/SSH を開き、コーディングを開始するには `node` と入力します。

- `while` ループと `yield` を使って、`start` から始まり `end` で終わる各値を返します。
- 既定のステップを `1` に設定する場合は、3 番目の引数を省略します。

```js
const rangeGenerator = function* (start, end, step = 1) {
  let i = start;
  while (i < end) {
    yield i;
    i += step;
  }
};
```

以下は、`rangeGenerator` 関数を使用する方法の例です。

```js
for (let i of rangeGenerator(6, 10)) console.log(i);
// 6, 7, 8, 9 が表示されます
```
