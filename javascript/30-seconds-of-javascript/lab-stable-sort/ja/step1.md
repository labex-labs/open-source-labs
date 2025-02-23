# 安定ソート

配列を安定ソートし、同じ値を持つ要素の初期インデックスを保つには、次の手順を実行します。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. `Array.prototype.map()` を使用して、入力配列の各要素をその対応するインデックスとペアにします。
3. `Array.prototype.sort()` と `compare` 関数を使用して、比較される要素が等しい場合に初期順序を保ちながらリストをソートします。
4. 再び `Array.prototype.map()` を使用して、配列要素を初期形式に戻します。
5. 元の配列は変更されず、代わりに新しい配列が返されます。

以下は、JavaScript での `stableSort` 関数の実装です。

```js
const stableSort = (arr, compare) =>
  arr
    .map((item, index) => ({ item, index }))
    .sort((a, b) => compare(a.item, b.item) || a.index - b.index)
    .map(({ item }) => item);
```

以下のように、配列と `compare` 関数を使用して `stableSort` 関数を呼び出すことで、ソートされた要素を持つ新しい配列を取得できます。

```js
const arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const stable = stableSort(arr, () => 0); // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
