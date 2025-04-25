# タイムゾーン付きで日付を ISO 形式に変換する

日付を拡張 ISO 形式（ISO 8601）に変換し、タイムゾーンオフセットを含めるには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを開始するために `node` を入力します。
2. `Date.prototype.getTimezoneOffset()` を使用してタイムゾーンオフセットを取得し、それを逆転させます。その符号を `diff` に格納します。
3. ヘルパー関数 `pad()` を定義します。これは、`Math.floor()` と `Math.abs()` を使用して渡された任意の数値を整数に正規化し、`String.prototype.padStart()` を使用してそれを 2 桁にパディングします。
4. `pad()` と `Date` プロトタイプの組み込みメソッドを使用して、タイムゾーンオフセット付きの ISO 8601 文字列を作成します。

次のコードを使用できます。

```js
const toISOStringWithTimezone = (date) => {
  const tzOffset = -date.getTimezoneOffset();
  const diff = tzOffset >= 0 ? "+" : "-";
  const pad = (n) => `${Math.floor(Math.abs(n))}`.padStart(2, "0");
  return (
    date.getFullYear() +
    "-" +
    pad(date.getMonth() + 1) +
    "-" +
    pad(date.getDate()) +
    "T" +
    pad(date.getHours()) +
    ":" +
    pad(date.getMinutes()) +
    ":" +
    pad(date.getSeconds()) +
    diff +
    pad(tzOffset / 60) +
    ":" +
    pad(tzOffset % 60)
  );
};
```

`toISOStringWithTimezone()` 関数に `new Date()` オブジェクトを引数として渡して、タイムゾーンオフセット付きの ISO 形式の日付を取得します。たとえば：

```js
toISOStringWithTimezone(new Date()); // '2020-10-06T20:43:33-04:00'
```
