# 条件を満たしたときに関数を適用する

特定の条件が満たされたときに関数を適用するには、`when`関数を使用します。まず、ターミナル/SSH を開き、`node`と入力します。

`when`関数は、1 つの引数を取り、引数が真であればコールバックを実行し、偽であれば引数を返す新しい関数を返します。この関数は単一の値`x`を期待し、`pred`パラメータに基づいて適切な値を返します。

以下は、`when`関数の例としての実装です。

```js
const when = (pred, whenTrue) => (x) => (pred(x) ? whenTrue(x) : x);
```

偶数を 2 倍にする新しい関数を作成するために`when`関数を使用できます。

```js
const doubleEvenNumbers = when(
  (x) => x % 2 === 0,
  (x) => x * 2
);
doubleEvenNumbers(2); // 4
doubleEvenNumbers(1); // 1
```
