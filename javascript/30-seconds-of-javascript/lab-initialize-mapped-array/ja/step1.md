# JavaScript でマッピングされた配列を初期化する

JavaScript でマッピングされた配列を初期化するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. `Array()` コンストラクタを使用して、必要な長さの配列を作成します。
3. `Array.prototype.fill()` を使用して、配列を `null` 値で埋めます。
4. `Array.prototype.map()` を使用して、提供された関数 `mapFn` を使って配列を必要な値で埋めます。
5. 2 番目の引数 `mapFn` を省略すると、各要素がそのインデックスにマッピングされます。

以下はコードの例です。

```js
const initializeMappedArray = (n, mapFn = (_, i) => i) =>
  Array(n).fill(null).map(mapFn);
```

必要な値でマッピングされた配列を作成するには、`initializeMappedArray` 関数を使用できます。

```js
initializeMappedArray(5); // [0, 1, 2, 3, 4]
initializeMappedArray(5, (i) => `item ${i + 1}`);
// ['item 1', 'item 2', 'item 3', 'item 4', 'item 5']
```
