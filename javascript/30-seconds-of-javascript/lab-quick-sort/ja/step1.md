# クイックソートアルゴリズム

コーディングの練習のために、ターミナル/SSH を開き、`node` と入力します。このアルゴリズムは、クイックソートアルゴリズムを使用して数値の配列をソートします。以下が実行する手順です。

- 再帰を使用します。
- スプレッド演算子 (`...`) を使用して元の配列 `arr` をクローンします。
- 配列の `length` が `2` 未満の場合、クローンした配列を返します。
- `Math.floor()` を使用してピボット要素のインデックスを計算します。
- `Array.prototype.reduce()` と `Array.prototype.push()` を使用して配列を 2 つのサブ配列に分割します。最初のサブ配列には、ピボット以下の要素が含まれ、2 番目のサブ配列には、ピボットより大きい要素が含まれます。結果を 2 つの配列に分解します。
- 作成したサブ配列に対して再帰的に `quickSort()` を呼び出します。

このアルゴリズムを実装する方法の例を以下に示します。

```js
const quickSort = (arr) => {
  const a = [...arr];
  if (a.length < 2) return a;
  const pivotIndex = Math.floor(arr.length / 2);
  const pivot = a[pivotIndex];
  const [lo, hi] = a.reduce(
    (acc, val, i) => {
      if (val < pivot || (val === pivot && i != pivotIndex)) {
        acc[0].push(val);
      } else if (val > pivot) {
        acc[1].push(val);
      }
      return acc;
    },
    [[], []]
  );
  return [...quickSort(lo), pivot, ...quickSort(hi)];
};
```

これをテストするには、次のコマンドを実行します。

```js
quickSort([1, 6, 1, 5, 3, 2, 1, 4]); // [1, 1, 1, 2, 3, 4, 5, 6]
```
