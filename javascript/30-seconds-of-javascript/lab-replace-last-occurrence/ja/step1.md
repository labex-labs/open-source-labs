# 問題の理解とセットアップ

コーディングを始める前に、`replaceLast` 関数が何をすべきかを理解しましょう。

1. 3 つのパラメータを受け取ります。

   - `str`: 変更する入力文字列
   - `pattern`: 検索する部分文字列または正規表現
   - `replacement`: 最後の出現箇所を置き換える文字列

2. パターンの最後の出現箇所が置き換えられた新しい文字列を返します。

関数を実装するための JavaScript ファイルを作成しましょう。

1. WebIDE のファイルエクスプローラーでプロジェクトディレクトリに移動します。
2. `replace-last` ディレクトリに `replaceLast.js` という名前の新しいファイルを作成します。
3. ファイルに次の基本構造を追加します。

```javascript
// Function to replace the last occurrence of a pattern in a string
function replaceLast(str, pattern, replacement) {
  // Our implementation will go here
  return str;
}

// We will add test cases here later
```

すべてが正しくセットアップされていることを確認するために、簡単なテストを追加しましょう。

```javascript
// Example usage
console.log(replaceLast("Hello world world", "world", "JavaScript"));
```

では、現在の出力を確認するためにコードを実行しましょう。

1. WebIDE でターミナルを開きます。
2. `replace-last` ディレクトリに移動します。
   ```bash
   cd ~/project/replace-last
   ```
3. Node.js を使用して JavaScript ファイルを実行します。
   ```bash
   node replaceLast.js
   ```

現在の関数は何も変更せずに元の文字列を返すため、出力には `Hello world world` が表示されるはずです。
