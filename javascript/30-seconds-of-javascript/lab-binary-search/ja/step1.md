# 二分探索アルゴリズム

コーディングの練習を始めるには、ターミナル/SSH を開き、`node` と入力します。二分探索アルゴリズムは、ソート済みの配列内の特定の要素のインデックスを見つけるために使用されます。二分探索アルゴリズムを実装する手順は以下の通りです。

1. 探索範囲の左端と右端を宣言し、それぞれ `l` と `r` として、それぞれ `0` と配列の `length` で初期化します。
2. `while` ループを使って、`Math.floor()` を使って探索サブ配列を半分に分割することで、繰り返し探索サブ配列を絞り込みます。
3. 要素が見つかった場合は、そのインデックスを返します。そうでなければ、`-1` を返します。
4. このアルゴリズムは、配列内の重複する値を考慮していません。

以下は、JavaScript での二分探索アルゴリズムの例の実装です。

```js
const binarySearch = (arr, item) => {
  let l = 0,
    r = arr.length - 1;
  while (l <= r) {
    const mid = Math.floor((l + r) / 2);
    const guess = arr[mid];
    if (guess === item) return mid;
    if (guess > item) r = mid - 1;
    else l = mid + 1;
  }
  return -1;
};
```

以下の例で `binarySearch` 関数をテストできます。

```js
binarySearch([1, 2, 3, 4, 5], 1); // 0
binarySearch([1, 2, 3, 4, 5], 5); // 4
binarySearch([1, 2, 3, 4, 5], 6); // -1
```
