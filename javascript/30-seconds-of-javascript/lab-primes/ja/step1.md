# エラトステネスの篩を使った素数の生成

エラトステネスの篩を使って、与えられた数までの素数を生成するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. `2` から与えられた数までの数字を含む配列を作成します。
3. `Array.prototype.filter()` を使って、`2` から与えられた数の平方根までの任意の数で割り切れる値をフィルタリングします。
4. 素数を含む結果の配列を返します。

与えられた数までの素数を生成する JavaScript コードは次のとおりです。

```js
const generatePrimes = (num) => {
  let arr = Array.from({ length: num - 1 }).map((x, i) => i + 2),
    sqrt = Math.floor(Math.sqrt(num)),
    numsTillSqrt = Array.from({ length: sqrt - 1 }).map((x, i) => i + 2);
  numsTillSqrt.forEach(
    (x) => (arr = arr.filter((y) => y % x !== 0 || y === x))
  );
  return arr;
};
```

必要な数を引数として渡すことで、`generatePrimes()` 関数を呼び出すことができます。たとえば：

```js
generatePrimes(10); // [2, 3, 5, 7]
```
