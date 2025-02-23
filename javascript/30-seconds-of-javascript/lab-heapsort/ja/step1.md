# ヒープソートアルゴリズム

コーディングを練習するには、ターミナル/SSH を開いて 'node' と入力します。次のアルゴリズムは、ヒープソートアルゴリズムを使用して数値の配列をソートします。以下の手順に従ってください。

- 関数内で再帰を使用します。
- スプレッド演算子 `(...)` を使用して元の配列 `arr` をクローンします。
- クロージャを使用して変数 `l` と関数 `heapify` を宣言します。
- `for` ループと `Math.floor()` を組み合わせて `heapify` を使用して、配列から最大ヒープを作成します。
- `for` ループを使用して、ソート対象の範囲を繰り返し狭め、必要に応じて `heapify` を使用して値を交換してクローンされた配列をソートします。

```js
const heapsort = (arr) => {
  const a = [...arr];
  let l = a.length;
  const heapify = (a, i) => {
    const left = 2 * i + 1;
    const right = 2 * i + 2;
    let max = i;
    if (left < l && a[left] > a[max]) max = left;
    if (right < l && a[right] > a[max]) max = right;
    if (max !== i) {
      [a[max], a[i]] = [a[i], a[max]];
      heapify(a, max);
    }
  };
  for (let i = Math.floor(l / 2); i >= 0; i -= 1) heapify(a, i);
  for (let i = a.length - 1; i > 0; i--) {
    [a[0], a[i]] = [a[i], a[0]];
    l--;
    heapify(a, 0);
  }
  return a;
};
```

例：

```js
heapsort([6, 3, 4, 1]); // [1, 3, 4, 6]
```
