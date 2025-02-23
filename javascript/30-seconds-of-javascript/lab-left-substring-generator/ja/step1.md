# コード実践: 左側の部分文字列生成器

与えられた文字列のすべての左側の部分文字列を生成するには、以下に示す `leftSubstrGenerator` 関数を使用します。

```js
const leftSubstrGenerator = function* (str) {
  if (!str.length) return;
  for (let i in str) yield str.slice(0, i + 1);
};
```

この関数を使用するには、ターミナル/SSH を開いて `node` と入力します。次に、文字列引数付きで関数を入力します。

```js
[...leftSubstrGenerator("hello")];
// [ 'h', 'he', 'hel', 'hell', 'hello' ]
```

この関数は、文字列が空の場合に早期に終了するために `String.prototype.length` を使用し、与えられた文字列の各部分文字列を先頭から始めて `yield` するために `String.prototype.slice()` を伴う `for...in` ループを使用しています。
