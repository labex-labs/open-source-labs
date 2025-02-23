# JavaScript でコンテキスト付きで関数を呼び出す方法

Node.js でコードを実行するには、ターミナル/SSH を開いて `node` と入力します。JavaScript で特定のコンテキストと一連の引数で関数を呼び出したい場合は、クロージャを使うことができます。以下がその方法です。

1. `key` と一連の `args` をパラメータとして受け取り、`context` パラメータを持つ新しい関数を返す `call` という名前の関数を定義します。

```js
const call =
  (key, ...args) =>
  (context) =>
    context[key](...args);
```

2. `call` 関数を使って、数値の配列に対して `map` 関数を呼び出します。この例では、`map` 関数は配列の各数値を 2 倍にします。

```js
Promise.resolve([1, 2, 3])
  .then(call("map", (x) => 2 * x))
  .then(console.log); // [ 2, 4, 6 ]
```

3. `call` 関数を特定のキー（たとえば `map`）にバインドして、数値の配列に対して `map` 関数を呼び出すこともできます。

```js
const map = call.bind(null, "map");
Promise.resolve([1, 2, 3])
  .then(map((x) => 2 * x))
  .then(console.log); // [ 2, 4, 6 ]
```

`call` 関数を使うことで、特定のコンテキストと引数のセットで任意の関数を簡単に呼び出すことができます。
