# 様々な日付形式でのテスト

基本的な検証関数ができたので、様々な入力に対する動作を理解するために、異なる日付形式でテストしてみましょう。

## テストスイートの作成

様々な日付形式を調べるための包括的なテストスイートを作成しましょう。

1. `dateTester.js` という名前の新しいファイルを作成します。
2. 以下のコードを追加します。

```javascript
// Import our isISOString function
const isISOString = require("./isISODate");

// Function to test different date strings
function testDate(description, dateString) {
  console.log(`Testing: ${description}`);
  console.log(`Input: "${dateString}"`);
  console.log(`Is ISO Format: ${isISOString(dateString)}`);
  console.log("-----------------------");
}

// Valid ISO date examples
testDate("Standard ISO date with timezone Z", "2023-05-12T14:30:15.123Z");
testDate("ISO date with zero milliseconds", "2020-10-12T10:10:10.000Z");

// Invalid or non-ISO format examples
testDate("Date only (no time component)", "2023-05-12");
testDate("Date and time without milliseconds", "2023-05-12T14:30:15Z");
testDate(
  "Date with time zone offset instead of Z",
  "2023-05-12T14:30:15+01:00"
);
testDate("Invalid date (month 13 does not exist)", "2023-13-12T14:30:15.123Z");
testDate("Non-date string", "Hello World");
```

3. ターミナルでテストスイートを実行します。

```bash
node dateTester.js
```

どの文字列が有効な ISO 日付で、どれが無効なのかを示す出力が表示されるはずです。

## 結果の理解

各テストケースが有効または無効になる理由を分析してみましょう。

1. `2023-05-12T14:30:15.123Z` - これは、UTC タイムゾーンの指示子 (Z) を含む完全な ISO 8601 形式に従っているため、有効です。

2. `2020-10-12T10:10:10.000Z` - ミリ秒が明示的に 000 に設定されているため、これも有効です。

3. `2023-05-12` - これは有効な日付ですが、時間の部分が欠けているため、ISO 形式ではありません。

4. `2023-05-12T14:30:15Z` - これは ISO 形式のように見えますが、厳密な ISO 形式では必須のミリ秒が欠けています。

5. `2023-05-12T14:30:15+01:00` - これは 'Z' の代わりにタイムゾーンのオフセット (+01:00) を使用しています。ISO 8601 では有効ですが、私たちの関数は `toISOString()` が生成する正確な形式（常に 'Z' を使用）を要求しています。

6. `2023-13-12T14:30:15.123Z` - これは無効な日付です（13 月は存在しません）。そのため、`new Date()` は無効な Date オブジェクトを作成します。

7. `Hello World` - これはまったく日付ではないため、`new Date()` は無効な Date オブジェクトを作成します。

私たちの検証関数は、具体的に 2 つの条件をチェックします。

1. 文字列は有効な日付に解析できなければなりません（NaN ではない）。
2. その日付を ISO 文字列に変換したとき、元の入力と完全に一致しなければなりません。

このアプローチにより、JavaScript の `toISOString()` メソッドが生成する正確な ISO 形式を検証できます。
