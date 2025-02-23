# 引数を追加する関数

受け取った引数に追加する関数を作成するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. スプレッド演算子 (`...`) を使って、`fn` の引数のリストに `partials` を追加します。
3. 次のコードを使って関数を作成します。

```js
const partialRight =
  (fn, ...partials) =>
  (...args) =>
    fn(...args, ...partials);
```

4. 例えば以下のように、関数をテストします。

```js
const greet = (greeting, name) => greeting + " " + name + "!";
const greetJohn = partialRight(greet, "John");
greetJohn("Hello"); // 'Hello John!'
```
