# 繰り返しジェネレーターを使ったコード練習

コーディングの練習をするには、ターミナル/SSH を開き、`node` と入力して、与えられた値を無限に繰り返すジェネレーターを作成します。`Generator.prototype.next()` が呼び出されるたびに値を `yield` する無限ループの `while` ループを使用します。そして、渡された値が `undefined` でない場合、`yield` 文の戻り値を使用して返される値を更新します。

```js
const repeatGenerator = function* (val) {
  let v = val;
  while (true) {
    let newV = yield v;
    if (newV !== undefined) v = newV;
  }
};
```

ジェネレーターをテストするには、値 `5` を使用してインスタンスを作成し、`repeater.next()` を呼び出してシーケンスの次の値を取得します。出力は `{ value: 5, done: false }` になります。再度 `repeater.next()` を呼び出すと、同じ値が返されます。値を変更するには、`repeater.next(4)` を呼び出します。これにより、`{ value: 4, done: false }` が返されます。最後に、`repeater.next()` を呼び出すと、更新された値 `{ value: 4, done: false }` が返されます。
