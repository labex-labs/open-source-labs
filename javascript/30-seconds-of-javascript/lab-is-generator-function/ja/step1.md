# 値がジェネレータ関数であるかどうかを確認する

値がジェネレータ関数であるかどうかを確認するには、`isGeneratorFunction` 関数を使用できます。コーディングの練習を始めるには、ターミナル/SSH を開いて `node` と入力します。

`isGeneratorFunction` 関数の動作方法は次のとおりです。

- `Object.prototype.toString()` と `Function.prototype.call()` を使って、与えられた引数がジェネレータ関数であるかどうかを確認します。
- チェックの結果が `'[object GeneratorFunction]'` の場合、その値はジェネレータ関数です。

`isGeneratorFunction` 関数のコードは次のとおりです。

```js
const isGeneratorFunction = (val) =>
  Object.prototype.toString.call(val) === "[object GeneratorFunction]";
```

そして、それを使用する方法のいくつかの例を示します。

```js
isGeneratorFunction(function () {}); // false
isGeneratorFunction(function* () {}); // true
```
