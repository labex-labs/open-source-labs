# 負のゼロのチェック

数値が負のゼロかどうかをチェックするには、ターミナル/SSH を開き、`node` を入力します。次に、以下のコードを使用します。

```js
const isNegativeZero = (val) => val === 0 && 1 / val === -Infinity;
```

これは、渡された値が `0` に等しいかどうか、および `1` をその値で割った結果が `-Infinity` に等しいかどうかをチェックします。例えば：

```js
isNegativeZero(-0); // true
isNegativeZero(0); // false
```
