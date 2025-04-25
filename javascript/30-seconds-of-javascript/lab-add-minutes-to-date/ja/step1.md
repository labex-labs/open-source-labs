# 日付に分を追加する関数

与えられた日付に特定の分を追加するには、次の関数を使用します。

```js
const addMinutesToDate = (date, n) => {
  // 与えられた日付から Date オブジェクトを作成する
  const d = new Date(date);
  // Date オブジェクトに n 分を追加する
  d.setTime(d.getTime() + n * 60000);
  // 新しい日付を yyyy-mm-dd HH:MM:SS 形式の文字列として返す
  return d.toISOString().split(".")[0].replace("T", " ");
};
```

この関数を使用するには、日付の文字列形式を最初の引数として渡し、追加する（または負の場合は減算する）分の数を 2 番目の引数として渡します。たとえば：

```js
addMinutesToDate("2020-10-19 12:00:00", 10); // '2020-10-19 12:10:00'
addMinutesToDate("2020-10-19", -10); // '2020-10-18 23:50:00'
```

関数は、`yyyy-mm-dd HH:MM:SS` 形式の文字列として新しい日付を返すことに注意してください。
