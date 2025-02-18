# パス文字列からネストされたオブジェクトのプロパティを取得する方法

コーディングの練習をするには、ターミナル/SSH を開き、`node` と入力します。

次の関数は、パス文字列で指定されたセレクタを使用して、オブジェクトから一連のプロパティを取得します。これを実現するには、次の手順に従います。

1. `Array.prototype.map()` を使用して各セレクタを反復処理し、`String.prototype.replace()` を適用して角括弧をドットに置き換えます。
2. `String.prototype.split()` を使用して各セレクタを文字列の配列に分割します。
3. `Array.prototype.filter()` を使用して空の値を削除します。
4. `Array.prototype.reduce()` を使用して各セレクタで示される値を取得します。

これが関数です。

```js
const get = (from, ...selectors) =>
  [...selectors].map((s) =>
    s
      .replace(/\[([^\[\]]*)\]/g, ".$1.")
      .split(".")
      .filter((t) => t !== "")
      .reduce((prev, cur) => prev && prev[cur], from)
  );
```

この関数を使用して、パス文字列でネストされたオブジェクトから値を取得することができます。次に例を示します。

```js
const obj = {
  selector: { to: { val: "val to select" } },
  target: [1, 2, { a: "test" }]
};
get(obj, "selector.to.val", "target[0]", "target[2].a");
// ['val to select', 1, 'test']
```
