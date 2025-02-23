# JavaScript で関数を合成する方法

JavaScript で関数合成を使ってコーディングを練習するには、ターミナル/SSH を開いて `node` と入力します。

以下は、JavaScript で右から左への関数合成を行う方法の例です。

1. `Array.prototype.reduce()` を使って右から左への関数合成を行います。
2. 最後の（最も右の）関数は 1 つ以上の引数を受け取ることができます。残りの関数は単項関数でなければなりません。
3. 任意の数の関数を引数として取り、それらを合成する新しい関数を返す `compose` 関数を定義します。
4. 必要な関数を必要な順序で `compose` 関数に渡します。
5. 必要な引数を使って新しい合成関数を呼び出します。

```js
const compose = (...fns) =>
  fns.reduce(
    (f, g) =>
      (...args) =>
        f(g(...args))
  );
```

たとえば、2 つの関数があるとしましょう。

```js
const add5 = (x) => x + 5;
const multiply = (x, y) => x * y;
```

これらの関数を `compose` を使って合成することができます。

```js
const multiplyAndAdd5 = compose(add5, multiply);
```

これで、必要な引数を使って `multiplyAndAdd5` を呼び出すことができます。

```js
multiplyAndAdd5(5, 2); // 15
```
