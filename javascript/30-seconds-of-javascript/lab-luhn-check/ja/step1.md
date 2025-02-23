# Luhn チェック

クレジットカード番号、IMEI 番号、National Provider Identifier 番号などの識別番号の検証に Luhn アルゴリズムを使用するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. 次のメソッドを組み合わせて使用して、数字の配列を取得します。`String.prototype.split()`、`Array.prototype.reverse()`、`Array.prototype.map()`、および `parseInt()`。
3. `Array.prototype.shift()` を使用して最後の桁を取得します。
4. `Array.prototype.reduce()` を使用して Luhn アルゴリズムを実装します。
5. `sum` が `10` で割り切れる場合は `true` を返し、それ以外の場合は `false` を返します。

以下がコードです。

```js
const luhnCheck = (num) => {
  const arr = (num + "")
    .split("")
    .reverse()
    .map((x) => parseInt(x));
  const lastDigit = arr.shift();
  let sum = arr.reduce(
    (acc, val, i) =>
      i % 2 !== 0 ? acc + val : acc + ((val *= 2) > 9 ? val - 9 : val),
    0
  );
  sum += lastDigit;
  return sum % 10 === 0;
};
```

次の例を使用して Luhn チェック関数をテストできます。

```js
luhnCheck("4485275742308327"); // true
luhnCheck(6011329933655299); //  true
luhnCheck(123456789); // false
```
