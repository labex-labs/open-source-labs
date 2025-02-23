# 関数合成の逆順

コーディングを練習するには、ターミナル/SSH を開き、`node` と入力します。

以下は、左から右への関数合成を行う方法です。

- `Array.prototype.reduce()` メソッドを使って、左から右への関数合成を行います。
- 最初の（最も左の）関数は 1 つ以上の引数を受け取ることができますが、残りの関数は単項関数でなければなりません。

```js
const composeRight = (...fns) =>
  fns.reduce(
    (f, g) =>
      (...args) =>
        g(f(...args))
  );
```

例えば：

```js
const add = (x, y) => x + y;
const square = (x) => x * x;
const addAndSquare = composeRight(add, square);
addAndSquare(1, 2); // 9
```
