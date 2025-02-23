# 条件が満たされるまで配列の末尾から要素を削除する

コーディングを練習するには、ターミナル/SSH を開いて `node` と入力します。

この関数は、渡された関数が `true` を返すまで配列の末尾から要素を削除し、その後削除された要素を返します。

その動作方法は以下の通りです。

- まず、スプレッド演算子 (`...`) と `Array.prototype.reverse()` を使って配列の逆順コピーを作成します。
- 次に、`Array.prototype.entries()` を使った `for...of` ループを使って逆順コピーをループ処理し、関数から返される値が真であるまで続けます。
- その後、`Array.prototype.slice()` を使って削除された要素を返します。
- コールバック関数 `fn` は、要素の値を 1 つの引数として受け取ります。

コードは以下の通りです。

```js
const takeRightUntil = (arr, fn) => {
  for (const [i, val] of [...arr].reverse().entries())
    if (fn(val)) return i === 0 ? [] : arr.slice(-i);
  return arr;
};
```

この関数の使い方の例は以下の通りです。

```js
takeRightUntil([1, 2, 3, 4], (n) => n < 3); // [3, 4]
```
