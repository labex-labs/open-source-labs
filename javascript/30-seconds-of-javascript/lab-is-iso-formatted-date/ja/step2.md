# ISO 形式の日付文字列を検証する関数の作成

このステップでは、与えられた文字列が有効な ISO 8601 形式であるかどうかをチェックする JavaScript 関数を作成します。

## 検証関数の作成

ISO 日付検証器用の新しい JavaScript ファイルを作成しましょう。

1. WebIDE で、左側のサイドバーにあるエクスプローラーアイコンをクリックします。
2. ファイルエクスプローラー内で右クリックし、「新しいファイル」を選択します。
3. ファイル名を `isISODate.js` と入力し、Enter キーを押します。
4. 以下のコードをファイルに追加します。

```javascript
/**
 * Checks if a string is a valid ISO 8601 formatted date string
 * @param {string} val - The string to check
 * @return {boolean} - Returns true if the string is in ISO format, false otherwise
 */
const isISOString = (val) => {
  // Create a Date object from the input string
  const d = new Date(val);

  // Check if the date is valid (not NaN) and if the ISO string matches the original
  return !Number.isNaN(d.valueOf()) && d.toISOString() === val;
};

// Export the function so we can use it elsewhere
module.exports = isISOString;
```

この関数がどのように動作するかを見てみましょう。

1. `new Date(val)` は入力文字列から Date オブジェクトを作成します。
2. `d.valueOf()` は数値のタイムスタンプ値（1970 年 1 月 1 日からのミリ秒数）を返します。
3. `Number.isNaN(d.valueOf())` は日付が無効であるかどうかをチェックします（NaN は「非数値」を意味します）。
4. `d.toISOString() === val` は、Date オブジェクトを ISO 文字列に変換した結果が元の入力と一致することを検証します。

## 関数のテスト

では、関数を試すための簡単なテストファイルを作成しましょう。

1. `testISO.js` という名前の別のファイルを作成します。
2. 以下のコードを追加します。

```javascript
// Import our isISOString function
const isISOString = require("./isISODate");

// Test with a valid ISO formatted date
console.log("Testing a valid ISO date:");
console.log("2020-10-12T10:10:10.000Z");
console.log("Result:", isISOString("2020-10-12T10:10:10.000Z"));
console.log();

// Test with an invalid format
console.log("Testing a non-ISO date:");
console.log("2020-10-12");
console.log("Result:", isISOString("2020-10-12"));
```

3. Node.js を使ってテストファイルを実行します。

```bash
node testISO.js
```

以下のような出力が表示されるはずです。

```
Testing a valid ISO date:
2020-10-12T10:10:10.000Z
Result: true

Testing a non-ISO date:
2020-10-12
Result: false
```

これは、私たちの関数が "2020-10-12T10:10:10.000Z" が有効な ISO 形式の日付であり、"2020-10-12" がそうでないことを正しく識別していることを示しています。
