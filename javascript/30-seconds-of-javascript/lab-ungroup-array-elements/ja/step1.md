# JavaScript で配列要素をグループ化解除する方法

`zip`関数で生成された配列の要素をグループ化解除するには、JavaScript の`unzip`関数を使って 2 次元配列を作成することができます。方法は以下の通りです。

1. ターミナル/SSH を開き、コーディングを練習するために`node`と入力します。
2. `Math.max()`、`Function.prototype.apply()`を使って配列内の最長のサブ配列を取得し、`Array.prototype.map()`を使って各要素を配列にします。
3. `Array.prototype.reduce()`と`Array.prototype.forEach()`を使って、グループ化された値を個々の配列にマッピングします。

以下が`unzip`関数のコードです。

```js
const unzip = (arr) =>
  arr.reduce(
    (acc, val) => (val.forEach((v, i) => acc[i].push(v)), acc),
    Array.from({
      length: Math.max(...arr.map((x) => x.length))
    }).map((x) => [])
  );
```

以下の例で`unzip`関数を使うことができます。

```js
unzip([
  ["a", 1, true],
  ["b", 2, false]
]); // [['a', 'b'], [1, 2], [true, false]]
unzip([
  ["a", 1, true],
  ["b", 2]
]); // [['a', 'b'], [1, 2], [true]]
```

これらの手順に従えば、JavaScript で簡単に配列要素をグループ化解除することができます。
