# 条件付きレンダリング

> VM 内には既に React プロジェクトが用意されています。一般的には、`App.js` にコードを追加するだけです。

依存関係をインストールするには、次のコマンドを使用してください。

```bash
npm i
```

React では、条件を記述するための特別な構文はありません。代わりに、通常の JavaScript コードを書くときと同じ技法を使用します。たとえば、`if` 文を使って条件付きで JSX を含めることができます。

```js
if (isPacked) {
  return <li className="item">{name} ✔</li>;
}
return <li className="item">{name}</li>;
```

もっとコンパクトなコードが好きな場合は、条件付き `?` 演算子を使うことができます。`if` とは異なり、これは JSX の中で機能します。

```js
return <li className="item">{isPacked ? name + " ✔" : name}</li>;
```

else ブランチが必要ない場合、より短い論理演算子 `&&` 構文を使うこともできます。

```js
return <li className="item">{isPacked && name + " ✔"}</li>;
```

`isPacked` プロップが `true` の場合、このコードは異なる JSX ツリーを返します。この変更により、一部の項目の末尾にチェックマークが付きます。

```js
// App.js
function Item({ name, isPacked }) {
  if (isPacked) {
    return <li className="item">{name} ✔</li>;
  }
  return <li className="item">{name}</li>;
}

export default function PackingList() {
  return (
    <section>
      <h1>Sally Ride's Packing List</h1>
      <ul>
        <Item isPacked={true} name="Space suit" />
        <Item isPacked={true} name="Helmet with a golden leaf" />
        <Item isPacked={false} name="Photo of Tam" />
      </ul>
    </section>
  );
}
```

プロジェクトを実行するには、次のコマンドを使用してください。その後、**Web 8080** タブを更新して Web ページをプレビューできます。

```bash
npm start
```
