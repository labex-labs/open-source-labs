# 数値検証関数

与えられた入力が数値かどうかを検証するには、次の手順に従います。

- ターミナル/SSHを開き、コーディングの練習を始めるために `node` と入力します。
- `parseFloat()` を使用して入力を数値に変換しようとします。
- `Number.isNaN()` と論理否定 (`!`) 演算子を使用して入力が数値かどうかをチェックします。
- `Number.isFinite()` を使用して入力が有限かどうかをチェックします。
- `Number` と緩やかな等価演算子 (`==`) を使用して型強制が成立するかどうかをチェックします。

以下が `validateNumber` 関数のコードです。

```js
const validateNumber = (input) => {
  const num = parseFloat(input);
  return !Number.isNaN(num) && Number.isFinite(num) && Number(input) == input;
};
```

`validateNumber` 関数を次のように使用できます。

```js
validateNumber("10"); // true
validateNumber("a"); // false
```
