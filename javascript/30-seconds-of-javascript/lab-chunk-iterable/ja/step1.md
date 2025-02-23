# イテラブルをチャンク化する

イテラブルを指定されたサイズの小さな配列にチャンク化するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. 与えられたイテラブルに対して `for...of` ループを使用し、`Array.prototype.push()` を使って各新しい値を現在の `chunk` に追加します。
3. `Array.prototype.length` を使って現在の `chunk` が望ましい `サイズ` になっているかどうかを確認し、その場合には値を `yield` します。
4. `Array.prototype.length` を使って最終的な `chunk` を確認し、空でない場合にはそれを `yield` します。
5. 次のコードを使用します。

```js
const chunkify = function* (itr, size) {
  let chunk = [];
  for (const v of itr) {
    chunk.push(v);
    if (chunk.length === size) {
      yield chunk;
      chunk = [];
    }
  }
  if (chunk.length) yield chunk;
};
```

6. このコードを使って関数をテストします。

```js
const x = new Set([1, 2, 1, 3, 4, 1, 2, 5]);
[...chunkify(x, 2)]; // [[1, 2], [3, 4], [5]]
```
