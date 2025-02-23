# 部分関数で前置された関数の引数

コーディングの練習を始めるには、ターミナル/SSH を開いて `node` を入力します。

関数 `partial` は、`partials` を最初の引数として `fn` を呼び出す新しい関数を作成するために使用されます。

- スプレッド演算子 (`...`) を使用して、`partials` を `fn` の引数のリストの先頭に追加します。

```js
const partial =
  (fn, ...partials) =>
  (...args) =>
    fn(...partials, ...args);
```

```js
const greet = (greeting, name) => greeting + " " + name + "!";
const greetHello = partial(greet, "Hello");
greetHello("John"); // 'Hello John!'
```
