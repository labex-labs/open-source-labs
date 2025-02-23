# マッピングされた配列の平均を計算するための指示

配列の平均を計算するには、提供された関数を使って各要素を新しい値にマッピングできます。以下が手順です。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. `Array.prototype.map()` を使って各要素を `fn` が返す値にマッピングします。
3. `Array.prototype.reduce()` を使って、初期値が `0` の累積器に各マッピングされた値を追加します。
4. 得られた配列をその長さで割って平均を求めます。

以下が使えるコードです。

```js
const averageBy = (arr, fn) =>
  arr
    .map(typeof fn === "function" ? fn : (val) => val[fn])
    .reduce((acc, val) => acc + val, 0) / arr.length;
```

この関数を以下の例を使ってテストできます。

```js
averageBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], (o) => o.n); // 5
averageBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], "n"); // 5
```
