# パイプを使った関数合成

パイプを使ったコーディングの練習を始めるには、ターミナル/SSH を開いて `node` と入力します。

`pipeFunctions` 関数は、展開演算子 (`...`) を使った `Array.prototype.reduce()` を使って左から右の関数合成を行います。最初の（最も左の）関数は 1 つ以上の引数を受け取ることができますが、残りの関数は単項関数でなければなりません。

```js
const pipeFunctions = (...fns) =>
  fns.reduce(
    (f, g) =>
      (...args) =>
        g(f(...args))
  );
```

ここでは、`pipeFunctions` を使って 2 つの数値を掛け算し、その結果に 5 を足す新しい関数 `multiplyAndAdd5` を作成する方法の例を示します。

```js
const add5 = (x) => x + 5;
const multiply = (x, y) => x * y;
const multiplyAndAdd5 = pipeFunctions(multiply, add5);
multiplyAndAdd5(5, 2); // 15
```

この例では、`multiplyAndAdd5` は 2 つの引数 `5` と `2` を受け取り、まずそれらに `multiply` を適用して `10` を得て、次にその結果に `add5` を適用して `15` を得る新しい関数です。
