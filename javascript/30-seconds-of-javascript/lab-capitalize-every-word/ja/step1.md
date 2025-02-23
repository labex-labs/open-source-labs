# JavaScript ですべての単語を大文字にする方法

JavaScript を使って文字列のすべての単語を大文字にするには、`String.prototype.replace()` メソッドを使って各単語の先頭文字を一致させ、その後 `String.prototype.toUpperCase()` メソッドを使ってそれを大文字にすることができます。

次に、使えるコードのサンプルを示します：

```js
const capitalizeEveryWord = (str) =>
  str.replace(/\b[a-z]/g, (char) => char.toUpperCase());
```

この関数を使うには、大文字にしたい文字列を引数として渡します。例えば：

```js
capitalizeEveryWord("hello world!"); // 'Hello World!'
```

これにより、大文字にされた文字列 'Hello World!' が返されます。
