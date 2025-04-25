# 日付が 2 つの日付の間にあるかどうかを確認する

日付が他の 2 つの日付の間にあるかどうかを確認するには、JavaScript のより大きい（`>`）と小さい（`<`）演算子を使います。以下は例の関数です。

```js
const isBetweenDates = (dateStart, dateEnd, date) =>
  date > dateStart && date < dateEnd;
```

この関数を使うには、開始日、終了日、確認する日付を渡します。日付が開始日と終了日の間にある場合、関数は`true`を返し、それ以外の場合は`false`を返します。以下はいくつかの例です。

```js
isBetweenDates(
  new Date(2010, 11, 20),
  new Date(2010, 11, 30),
  new Date(2010, 11, 19)
); // false

isBetweenDates(
  new Date(2010, 11, 20),
  new Date(2010, 11, 30),
  new Date(2010, 11, 25)
); // true
```

コーディングの練習を始めるには、ターミナル/SSH を開いて`node`と入力します。
