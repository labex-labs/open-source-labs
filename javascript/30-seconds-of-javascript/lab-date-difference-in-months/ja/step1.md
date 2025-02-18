# 月数での日付差を計算する関数

2 つの日付の月数の差を計算するには、次の関数を使用します。

```js
const getMonthsDiffBetweenDates = (dateInitial, dateFinal) =>
  Math.max(
    (dateFinal.getFullYear() - dateInitial.getFullYear()) * 12 +
      dateFinal.getMonth() -
      dateInitial.getMonth(),
    0
  );
```

この関数を使用するには、2 つの `Date` オブジェクトを引数として渡します。例えば：

```js
getMonthsDiffBetweenDates(new Date("2017-12-13"), new Date("2018-04-29")); // 4
```

この関数は、`Date.prototype.getFullYear()` と `Date.prototype.getMonth()` メソッドを使用して、2 つの日付の月数の差を計算します。
