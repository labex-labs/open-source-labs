# 英数字文字列をチェックする他の方法を探索する

正規表現を使用する以外にも、文字列が英数字であるかどうかをチェックする方法は他にもあります。`alternative-methods.js` という名前の新しいファイルを作成して、それらのいくつかを探索しましょう。

1. ファイルエクスプローラーパネル内で右クリックします。
2. 「New File」を選択します。
3. ファイル名を `alternative-methods.js` とします。

ファイルに以下のコードを追加します。

```javascript
// Method 1: Using regular expression (our original method)
function isAlphaNumericRegex(str) {
  return /^[a-zA-Z0-9]+$/.test(str);
}

// Method 2: Using Array.every() and checking each character
function isAlphaNumericEvery(str) {
  // If string is empty, return false
  if (str.length === 0) return false;

  return [...str].every((char) => {
    const code = char.charCodeAt(0);
    // Check if character is a digit (0-9)
    const isDigit = code >= 48 && code <= 57;
    // Check if character is a lowercase letter (a-z)
    const isLowercase = code >= 97 && code <= 122;
    // Check if character is an uppercase letter (A-Z)
    const isUppercase = code >= 65 && code <= 90;

    return isDigit || isLowercase || isUppercase;
  });
}

// Method 3: Using a combination of match() and length
function isAlphaNumericMatch(str) {
  // If string is empty, return false
  if (str.length === 0) return false;

  // Remove all alphanumeric characters and check if anything remains
  const nonAlphaNumeric = str.match(/[^a-zA-Z0-9]/g);
  return nonAlphaNumeric === null;
}

// Test strings
const testStrings = [
  "hello123",
  "HELLO123",
  "hello 123",
  "hello@123",
  "",
  "0123456789",
  "abcdefghijklmnopqrstuvwxyz"
];

// Test each method with each string
console.log("=== Testing Different Methods ===");
console.log("String\t\t\tRegex\tEvery\tMatch");
console.log("---------------------------------------------");

testStrings.forEach((str) => {
  const displayStr = str.length > 10 ? str.substring(0, 10) + "..." : str;
  const paddedStr = displayStr.padEnd(16, " ");

  const regexResult = isAlphaNumericRegex(str);
  const everyResult = isAlphaNumericEvery(str);
  const matchResult = isAlphaNumericMatch(str);

  console.log(`"${paddedStr}"\t${regexResult}\t${everyResult}\t${matchResult}`);
});

console.log("\nPerformance Comparison:");
const iterations = 1000000;
const testString = "hello123ABCxyz45";

console.time("Regex Method");
for (let i = 0; i < iterations; i++) {
  isAlphaNumericRegex(testString);
}
console.timeEnd("Regex Method");

console.time("Every Method");
for (let i = 0; i < iterations; i++) {
  isAlphaNumericEvery(testString);
}
console.timeEnd("Every Method");

console.time("Match Method");
for (let i = 0; i < iterations; i++) {
  isAlphaNumericMatch(testString);
}
console.timeEnd("Match Method");
```

ファイルを保存し、以下のコマンドで実行します。

```bash
node alternative-methods.js
```

出力結果には、各メソッドが異なるテスト文字列に対してどのように動作するか、およびメソッド間のパフォーマンス比較が表示されます。正規表現を使用するメソッドは通常、最も簡潔で、多くの場合最速ですが、代替アプローチを理解することも有用です。

各メソッドを見てみましょう。

1. `isAlphaNumericRegex`：正規表現を使用して、英数字のみにマッチさせます。
2. `isAlphaNumericEvery`：各文字の ASCII コードをチェックして、それが英数字であるかどうかを判断します。
3. `isAlphaNumericMatch`：すべての英数字を削除し、残ったものがあるかどうかをチェックします。

異なるアプローチを理解することで、プログラミングの問題を解決する際に柔軟性が高まります。正規表現は強力ですが、読みにくいことがあります。他のメソッドは、特に正規表現パターンに慣れていないプログラマーにとって、より直感的である可能性があります。
