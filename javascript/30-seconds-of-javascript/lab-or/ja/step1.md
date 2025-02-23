# JavaScript における論理和演算子の使用

コーディングの練習を始めるには、ターミナル/SSH を開き、`node` を入力します。論理和演算子 (`||`) は、与えられた引数の少なくとも 1 つが `true` であるかどうかをチェックします。

以下は、論理和演算子を使用する例です。

```js
const or = (a, b) => a || b;
```

また、この演算子を使用したときの出力の例をいくつか示します。

```js
or(true, true); // true
or(true, false); // true
or(false, false); // false
```
