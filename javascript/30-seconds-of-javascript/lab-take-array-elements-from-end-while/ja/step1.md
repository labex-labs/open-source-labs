# 条件が満たされるまで配列の末尾から要素を削除する

コーディングの練習を始めるには、ターミナル/SSH を開いて`node`と入力します。

ここに、渡された関数が`false`を返すまで配列の末尾から要素を削除する関数があります。その後、削除された要素を返します。

これを使用するには、スプレッド演算子 (`...`) と `Array.prototype.reverse()` を使用して配列の逆順コピーを作成します。次に、`Array.prototype.entries()` を使った `for...of` ループを使って逆順コピーをループ処理し、関数から返される値が偽でなくなるまで続けます。

コールバック関数 `fn` は、要素の値を 1 つの引数として受け取ります。最後に、`Array.prototype.slice()` を使って削除された要素を返します。

```js
const takeRightWhile = (arr, fn) => {
  for (const [i, val] of [...arr].reverse().entries())
    if (!fn(val)) return i === 0 ? [] : arr.slice(-i);
  return arr;
};
```

この関数の使い方の例を以下に示します。

```js
takeRightWhile([1, 2, 3, 4], (n) => n >= 3); // [3, 4]
```
