# 文字列内の空白文字の確認

文字列に空白文字が含まれているかどうかを確認するには、以下の手順に従います。

- ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
- 適切な正規表現を使って `RegExp.prototype.test()` を使って、与えられた文字列に空白文字が含まれているかどうかを確認します。
- 以下はコードの例です。

  ```js
  const containsWhitespace = (str) => /\s/.test(str);
  ```

- 関数をテストするには、文字列引数で `containsWhitespace` を呼び出します。文字列に空白文字が含まれている場合は `true` を返し、そうでない場合は `false` を返します。

  ```js
  containsWhitespace("lorem"); // false
  containsWhitespace("lorem ipsum"); // true
  ```
