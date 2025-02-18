# リストのレンダリング

> VM にはすでに React プロジェクトが用意されています。一般的には、`App.js` にコードを追加するだけです。

以下のコマンドを使用して依存関係をインストールしてください。

```bash
npm i
```

コンポーネントのリストをレンダリングするには、for ループや配列の `map()` 関数などの JavaScript の機能を利用します。

たとえば、商品の配列があるとしましょう。

```js
const products = [
  { title: "Cabbage", id: 1 },
  { title: "Garlic", id: 2 },
  { title: "Apple", id: 3 }
];
```

コンポーネント内で `map()` 関数を使用して、商品の配列を `<li>` 要素の配列に変換します。

```js
const listItems = products.map((product) => (
  <li key={product.id}>{product.title}</li>
));

return <ul>{listItems}</ul>;
```

`<li>` に `key` 属性があることに注意してください。リスト内の各アイテムには、兄弟要素の中でそのアイテムを一意に識別する文字列または数値を渡す必要があります。通常、キーはデータベースの ID など、データから取得する必要があります。React はキーを使用して、後でアイテムを挿入、削除、または並べ替えた場合に何が起こったかを把握します。

```js
// App.js
const products = [
  { title: "Cabbage", isFruit: false, id: 1 },
  { title: "Garlic", isFruit: false, id: 2 },
  { title: "Apple", isFruit: true, id: 3 }
];

export default function ShoppingList() {
  const listItems = products.map((product) => (
    <li
      key={product.id}
      style={{
        color: product.isFruit ? "magenta" : "darkgreen"
      }}
    >
      {product.title}
    </li>
  ));

  return <ul>{listItems}</ul>;
}
```

プロジェクトを実行するには、以下のコマンドを使用します。その後、**Web 8080** タブを更新すると、Web ページをプレビューできます。

```bash
npm start
```
