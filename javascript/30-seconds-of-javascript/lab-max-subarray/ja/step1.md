# 最大部分配列アルゴリズム

コーディングを練習するには、ターミナル/SSH を開いて `node` と入力します。このアルゴリズムは、数値の配列内で最大の合計を持つ連続する部分配列を見つけます。このアルゴリズムを実装するには、次の手順に従います。

- 貪欲法を使用して、現在の `sum` と現在の最大値 `maxSum` を追跡します。すべての値が負の場合、最も高い負の値が返されるように、`maxSum` を `-Infinity` に設定します。
- 最大開始インデックス `sMax`、最大終了インデックス `eMax`、および現在の開始インデックス `s` を追跡するための変数を定義します。
- `Array.prototype.forEach()` を使用して値を反復処理し、現在の値を `sum` に追加します。
- 現在の `sum` が `maxSum` より大きい場合、インデックス値と `maxSum` を更新します。
- `sum` が 0 未満の場合、それを 0 にリセットし、`s` の値を次のインデックスに更新します。
- `Array.prototype.slice()` を使用して、インデックス変数によって示される部分配列を返します。

ここに、このアルゴリズムの JavaScript コードがあります。

```js
const maxSubarray = (...arr) => {
  let maxSum = -Infinity,
    sum = 0;
  let sMax = 0,
    eMax = arr.length - 1,
    s = 0;

  arr.forEach((n, i) => {
    sum += n;
    if (maxSum < sum) {
      maxSum = sum;
      sMax = s;
      eMax = i;
    }

    if (sum < 0) {
      sum = 0;
      s = i + 1;
    }
  });

  return arr.slice(sMax, eMax + 1);
};
```

ここに、この関数の使用方法の例があります。

```js
maxSubarray(-2, 1, -3, 4, -1, 2, 1, -5, 4); // [4, -1, 2, 1]
```
