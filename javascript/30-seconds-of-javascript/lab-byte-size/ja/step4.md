# 実用的なサンプルファイルの作成

では、JavaScript ファイルを作成して、バイトサイズを計算する関数をより実用的な形で実装しましょう。これにより、この関数を実際のアプリケーションでどのように使用するかがわかります。

1. WebIDE で新しいファイルを作成します。ファイルエクスプローラーのサイドバーにある「New File」アイコンをクリックし、`byteSizeCalculator.js` と名付けます。

2. 以下のコードをファイルに追加します。

```javascript
/**
 * 与えられた文字列のバイトサイズを計算します。
 * @param {string} str - バイトサイズを計算する文字列。
 * @returns {number} バイト単位のサイズ。
 */
function calculateByteSize(str) {
  return new Blob([str]).size;
}

// 異なるタイプの文字列の例
const examples = [
  "Hello World",
  "😀",
  "The quick brown fox jumps over the lazy dog",
  "123!@#$%^&*()",
  "Hello, 世界!",
  "😀😃😄😁"
];

// 結果を表示する
console.log("String Byte Size Calculator\n");
console.log("String".padEnd(45) + "| Characters | Bytes");
console.log("-".repeat(70));

examples.forEach((example) => {
  console.log(
    `"${example}"`.padEnd(45) +
      `| ${example.length}`.padEnd(12) +
      `| ${calculateByteSize(example)}`
  );
});
```

3. Ctrl+S を押すか、メニューから「File > Save」を選択してファイルを保存します。

4. ターミナルからファイルを実行します。

```bash
node byteSizeCalculator.js
```

以下のような出力が表示されるはずです。

```
String Byte Size Calculator

String                                      | Characters | Bytes
----------------------------------------------------------------------
"Hello World"                               | 11         | 11
"😀"                                        | 1          | 4
"The quick brown fox jumps over the lazy dog" | 43         | 43
"123!@#$%^&*()"                            | 13         | 13
"Hello, 世界!"                              | 10         | 13
"😀😃😄😁"                                  | 4          | 16
```

この表は、異なるタイプの文字列における文字数とバイトサイズの違いを明確に示しています。

これらの違いを理解することは、以下のような場合に重要です。

- Web フォームでのユーザー入力の制限を設定するとき
- テキストデータのストレージ要件を計算するとき
- サイズ制限のある API を使用するとき
- ネットワークを介したデータ転送を最適化するとき
