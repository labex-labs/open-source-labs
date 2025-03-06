# 各単語の大文字化

これで文字列が単語に分割できるようになったので、各単語の最初の文字を大文字にし、残りを小文字にする必要があります。この機能を実装してみましょう。

1. Node.js セッションで、単一の単語を大文字化する関数を書いてみましょう。以下を入力します。

```javascript
function capitalizeWord(word) {
  return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
}

// Test with a few examples
console.log(capitalizeWord("hello"));
console.log(capitalizeWord("WORLD"));
console.log(capitalizeWord("javaScript"));
```

出力は以下のようになるはずです。

```
Hello
World
Javascript
```

2. 次に、`map()` メソッドを使用して、この関数を単語の配列に適用しましょう。以下を入力します。

```javascript
let words = ["hello", "WORLD", "javaScript"];
let capitalizedWords = words.map((word) => capitalizeWord(word));
console.log(capitalizedWords);
```

出力は以下のようになるはずです。

```
[ 'Hello', 'World', 'Javascript' ]
```

`map()` メソッドは、元の配列の各要素に関数を適用して新しい配列を作成します。この場合、`capitalizeWord` 関数を各単語に適用しています。

3. 最後に、大文字化された単語を結合してパスカルケース (Pascal case) の文字列を作成しましょう。

```javascript
let pascalCase = capitalizedWords.join("");
console.log(pascalCase);
```

出力は以下のようになるはずです。

```
HelloWorldJavascript
```

`join("")` メソッドは、配列のすべての要素を 1 つの文字列に結合し、各要素の間に指定された区切り文字 (この場合は空文字列) を使用します。

これらの手順は、文字列をパスカルケースに変換する核心的なプロセスを示しています。

1. 文字列を単語に分割する
2. 各単語を大文字化する
3. 区切り文字なしで単語を結合する
