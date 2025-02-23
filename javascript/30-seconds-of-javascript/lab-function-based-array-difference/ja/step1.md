# 関数に基づいて配列から値をフィルタリングする方法

与えられた比較関数に基づいて配列からすべての値をフィルタリングするには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. `Array.prototype.filter()` と `Array.prototype.findIndex()` を使用して適切な値を見つけます。
3. デフォルトの厳密等値比較関数を使用するには、最後の引数 `comp` を省略します。
4. 次のコードを使用します。

```js
const differenceWith = (arr, val, comp = (a, b) => a === b) =>
  arr.filter((a) => val.findIndex((b) => comp(a, b)) === -1);
```

5. 次の例を使用して関数をテストします。

```js
differenceWith(
  [1, 1.2, 1.5, 3, 0],
  [1.9, 3, 0],
  (a, b) => Math.round(a) === Math.round(b)
); // 予想される出力: [1, 1.2]

differenceWith([1, 1.2, 1.3], [1, 1.3, 1.5]); // 予想される出力: [1.2]
```
