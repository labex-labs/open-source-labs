# 右側の部分文字列生成器

与えられた文字列のすべての右側の部分文字列を生成するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. 文字列が空の場合、`String.prototype.length` を使用して反復処理を早期に停止します。
3. `for...in` ループと `String.prototype.slice()` を使用して、与えられた文字列の各部分文字列を末尾から始めて `yield` します。

以下はコードの断片です。

```js
const rightSubstrGenerator = function* (str) {
  if (!str.length) return;
  for (let i in str) yield str.slice(-i - 1);
};
```

使用例：

```js
[...rightSubstrGenerator("hello")];
// [ 'o', 'lo', 'llo', 'ello', 'hello' ]
```
