# 文字列を単語の配列に変換する関数

与えられた文字列を単語の配列に変換するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. 文字列の配列に変換するには、`String.prototype.split()` メソッドに提供された `pattern`（デフォルトは正規表現として非アルファベット）を使用します。
3. 空の文字列を削除するには、`Array.prototype.filter()` メソッドを使用します。
4. デフォルトの正規表現を使用するには、2 番目の引数 `pattern` を省略します。

これらの手順を実装する関数は次のとおりです。

```js
const words = (str, pattern = /[^a-zA-Z-]+/) =>
  str.split(pattern).filter(Boolean);
```

文字列を単語の配列に変換するには、さまざまな文字列を使って `words()` 関数を使用できます。

```js
words("I love javaScript!!"); // ['I', 'love', 'javaScript']
words("python, javaScript & coffee"); // ['python', 'javaScript', 'coffee']
```
