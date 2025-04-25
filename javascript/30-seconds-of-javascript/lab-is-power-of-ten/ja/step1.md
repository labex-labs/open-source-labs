# 数が 10 の累乗かどうかを確認する

数が 10 の累乗かどうかを確認するには、ターミナル/SSH を開いて`node`と入力します。

`n`が 10 の累乗かどうかを判断するために使用できるコードは次のとおりです。

```js
const isPowerOfTen = (n) => Math.log10(n) % 1 === 0;
```

与えられた数が 10 の累乗かどうかを判断するには、`isPowerOfTen()`関数を使用します。

```js
isPowerOfTen(1); // true
isPowerOfTen(10); // true
isPowerOfTen(20); // false
```
