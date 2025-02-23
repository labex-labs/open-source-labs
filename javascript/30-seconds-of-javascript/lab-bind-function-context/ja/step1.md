# 与えられたコンテキストで関数を作成する

与えられたコンテキストで関数を作成するには、`bind` 関数を使用します。まず、ターミナル/SSH を開き、`node` と入力します。

`bind` 関数は、与えられたコンテキストで元の関数を呼び出す新しい関数を作成します。また、任意で、追加の提供されたパラメータを引数の先頭に追加することもできます。

`bind` を使用するには、元の関数 (`fn`) と望ましいコンテキスト (`context`) を渡します。また、関数にバインドする必要のある任意の追加のパラメータ (`...boundArgs`) も渡すことができます。

`bind` 関数は、与えられた `context` を `fn` に適用するために `Function.prototype.apply()` を使用する新しい関数を返します。また、スプレッド演算子 (`...`) を使用して、追加の提供されたパラメータを引数の先頭に追加します。

以下は、`bind` の使用例です。

```js
const bind =
  (fn, context, ...boundArgs) =>
  (...args) =>
    fn.apply(context, [...boundArgs, ...args]);

function greet(greeting, punctuation) {
  return greeting + " " + this.user + punctuation;
}

const freddy = { user: "fred" };
const freddyBound = bind(greet, freddy);
console.log(freddyBound("hi", "!")); // 'hi fred!'
```

この例では、2 つのパラメータ (`greeting` と `punctuation`) を受け取り、`greeting`、現在のコンテキスト (`this`) の `user` プロパティ、および `punctuation` を連結した文字列を返す `greet` 関数を定義しています。

次に、`user` プロパティが `'fred'` に設定された新しいオブジェクト (`freddy`) を作成します。

最後に、`bind` を使用して新しい関数 (`freddyBound`) を作成し、`greet` 関数と望ましいコンテキストとして `freddy` オブジェクトを渡します。その後、2 つの追加のパラメータ (`'hi'` と `'!'`) を使用して `freddyBound` を呼び出すことができ、これらはバインドされた `freddy` コンテキストとともに元の `greet` 関数に渡されます。結果の出力は `'hi fred!'` です。
