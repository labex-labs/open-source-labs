# 選択ソートアルゴリズム

コーディングを始めるには、ターミナル/SSH を開き、`node` と入力します。

次の関数は、選択ソートアルゴリズムを使用して数値の配列をソートします。

```js
const selectionSort = (arr) => {
  const a = [...arr];
  for (let i = 0; i < a.length; i++) {
    const min = a
      .slice(i + 1)
      .reduce((acc, val, j) => (val < a[acc] ? j + i + 1 : acc), i);
    if (min !== i) [a[i], a[min]] = [a[min], a[i]];
  }
  return a;
};
```

この関数を使用するには、数値の配列を `selectionSort()` に渡します。例えば：

```js
selectionSort([5, 1, 4, 2, 3]); // [1, 2, 3, 4, 5]
```

この関数は、スプレッド演算子 (`...`) を使用して元の配列をクローンします。その後、`for` ループを使用して配列を反復処理します。`Array.prototype.slice()` と `Array.prototype.reduce()` を使用して、現在のインデックスの右側のサブ配列内の最小要素のインデックスを見つけます。必要に応じて、スワップを行います。
