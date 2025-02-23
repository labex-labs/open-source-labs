# 月の日数を取得するJavaScript関数

JavaScriptを使って指定された年の特定の月の日数を求めるには、次の手順に従います。

1. ターミナル/SSHを開き、コーディングを練習するために`node`と入力します。
2. `daysInMonth`という名前の関数を作成し、2つのパラメーター`year`と`month`を受け取ります。
3. `daysInMonth`関数の中で、`Date`コンストラクタを使って、与えられた`year`と`month`から日付オブジェクトを作成します。
4. 月は0から始まるため、前月の最終日を取得するために、日付パラメーターを`0`に設定します。
5. `Date.prototype.getDate()`を使って、与えられた`month`の日数を返します。
6. `daysInMonth`関数から日数を返します。

以下は`daysInMonth`関数のJavaScriptコードです。

```js
const daysInMonth = (year, month) => new Date(year, month, 0).getDate();
```

次の例のように、`daysInMonth`関数を使って任意の年の任意の月の日数を取得することができます。

```js
daysInMonth(2020, 12); // 31
daysInMonth(2024, 2); // 29
```
