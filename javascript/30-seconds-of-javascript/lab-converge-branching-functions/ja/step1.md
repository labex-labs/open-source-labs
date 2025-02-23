# 収束関数

コーディングを練習するには、ターミナル/SSH を開き、`node` と入力します。

この関数 `converge` は、収束関数と分岐関数のリストを入力として受け取ります。それは、各分岐関数を入力引数に適用する新しい関数を返します。次に、分岐関数の結果が引数として収束関数に渡されます。

`Array.prototype.map()` と `Function.prototype.apply()` メソッドを使用して、各関数を入力引数に適用します。その後、スプレッド演算子 (`...`) を使用して、他のすべての関数の結果で `converger` を呼び出します。

以下が `converge` 関数のコードです。

```js
const converge =
  (converger, fns) =>
  (...args) =>
    converger(...fns.map((fn) => fn.apply(null, args)));
```

この関数を使用する方法の例を以下に示します。`average` 関数は、配列の平均を計算する匿名関数を使って `converge` を呼び出すことで作成されます。分岐関数は、それぞれ配列の合計とその長さを計算する 2 つの匿名関数です。

```js
const average = converge(
  (a, b) => a / b,
  [(arr) => arr.reduce((a, v) => a + v, 0), (arr) => arr.length]
);
average([1, 2, 3, 4, 5, 6, 7]); // 4
```

このコードは配列 `[1, 2, 3, 4, 5, 6, 7]` の平均を計算し、`4` を返します。
