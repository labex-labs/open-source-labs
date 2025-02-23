# オブジェクトメソッドをバインドする関数

オブジェクトメソッドをそのコンテキストにバインドし、任意で追加のパラメータを先頭に追加する関数を作成するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. オブジェクトコンテキスト、メソッドキー、および先頭に追加する任意の追加引数を受け取る関数を定義します。
3. 関数は、`Function.prototype.apply()` を使用してメソッドをオブジェクトコンテキストにバインドする新しい関数を返す必要があります。
4. スプレッド演算子 (`...`) を使用して、任意の追加で提供されたパラメータを引数の先頭に追加します。
5. 以下は、例となる実装です。

```js
const bindKey =
  (context, fn, ...boundArgs) =>
  (...args) =>
    context[fn].apply(context, [...boundArgs, ...args]);
```

6. 関数をテストするには、メソッドを持つオブジェクトを作成し、`bindKey()` を使用してバインドします。その後、いくつかの引数でバインドされたメソッドを呼び出します。

```js
const freddy = {
  user: "fred",
  greet: function (greeting, punctuation) {
    return greeting + " " + this.user + punctuation;
  }
};
const freddyBound = bindKey(freddy, "greet");
console.log(freddyBound("hi", "!")); // 'hi fred!'
```
