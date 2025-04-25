# JavaScript での日付計算の理解

これで `Date` オブジェクトの作成方法がわかったので、2 つの日付の差を計算する方法を学んでみましょう。

## JavaScript での日付演算

JavaScript では、`Date` オブジェクトに対して直接算術演算を行うことができます。ある `Date` オブジェクトから別の `Date` オブジェクトを引くと、JavaScript は自動的にそれらをタイムスタンプ（ミリ秒）に変換して減算を行います。

```javascript
let date1 = new Date("2023-01-01T00:00:00");
let date2 = new Date("2023-01-01T00:01:00");

let differenceInMilliseconds = date2 - date1;
console.log(differenceInMilliseconds); // 60000 (60 seconds * 1000 milliseconds)
```

このコードを Node.js 環境で実行してみてください。結果は `60000` になり、これは 60 秒をミリ秒で表したものです。

## ミリ秒を秒に変換する

時間差をミリ秒から秒に変換するには、単に 1000 で割ればいいです。

```javascript
let differenceInSeconds = differenceInMilliseconds / 1000;
console.log(differenceInSeconds); // 60
```

これにより、時間差が秒単位で得られます。この例では 60 秒、つまり 1 分です。

## 日付差を計算する関数の作成

ここまでの概念が理解できたので、2 つの日付の差を秒単位で計算する簡単な関数を作成してみましょう。

```javascript
function getDateDifferenceInSeconds(startDate, endDate) {
  return (endDate - startDate) / 1000;
}

// Test the function
let start = new Date("2023-01-01T00:00:00");
let end = new Date("2023-01-01T00:01:30");
let difference = getDateDifferenceInSeconds(start, end);
console.log(difference); // 90 (1 minute and 30 seconds)
```

この関数を Node.js 環境で入力して実行してみてください。結果は `90` になり、これは 1 分 30 秒を表しています。
