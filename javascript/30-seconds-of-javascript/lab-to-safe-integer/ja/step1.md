# 値を安全な整数に変換する

値を安全な整数に変換するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. `Math.max()` と `Math.min()` を使用して、最も近い安全な値を見つけます。
3. `Math.round()` を使用して、値を整数に変換します。

値を安全な整数に変換する方法を示すコード スニペットの例を次に示します。

```js
const toSafeInteger = (num) =>
  Math.round(
    Math.max(Math.min(num, Number.MAX_SAFE_INTEGER), Number.MIN_SAFE_INTEGER)
  );
```

この関数を次の入力でテストできます。

```js
toSafeInteger("3.2"); // 3
toSafeInteger(Infinity); // 9007199254740991
```
