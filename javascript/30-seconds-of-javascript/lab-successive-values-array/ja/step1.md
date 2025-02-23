# 順次値の配列

JavaScript で順次値の配列を作成するには、`Array.prototype.reduce()` メソッドを使うことができます。このメソッドは、左から右へと、関数をアキュムレータと配列の各要素に適用し、順次減算された値の配列を返します。

以下は、与えられた関数を与えられた配列に適用し、各新しい結果を格納するための `reduceSuccessive` 関数の使い方です：

```js
const reduceSuccessive = (arr, fn, acc) =>
  arr.reduce(
    (res, val, i, arr) => (res.push(fn(res.slice(-1)[0], val, i, arr)), res),
    [acc]
  );
```

その後、配列、関数、およびアキュムレータの初期値を使って `reduceSuccessive` 関数を呼び出すことができます：

```js
reduceSuccessive([1, 2, 3, 4, 5, 6], (acc, val) => acc + val, 0);
// [0, 1, 3, 6, 10, 15, 21]
```

この関数を使ってコーディングを練習するには、ターミナル/SSH を開いて `node` と入力します。
