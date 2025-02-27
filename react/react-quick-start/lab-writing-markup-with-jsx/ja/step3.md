# スタイルの追加

React では、`className` を使って CSS クラスを指定します。これは HTML の [class](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/class) 属性と同じように機能します。

```html
<img className="avatar" />
```

その後、別の CSS ファイルに CSS ルールを記述します。

```css
/* App.css */
.avatar {
  border-radius: 50%;
}
```

React では、CSS ファイルを追加する方法を規定していません。最も簡単な場合、HTML に `<link>` タグを追加します。ビルドツールやフレームワークを使用する場合は、そのドキュメントを参照して、プロジェクトに CSS ファイルを追加する方法を学んでください。

```js
// App.js
import "./App.css";
```

JSX の波括弧の中には、より複雑な式を記述することもできます。たとえば、[文字列連結](https://javascript.info/operators#string-concatenation-with-binary) です。

```js
// App.js
const user = {
  name: "Hedy Lamarr",
  imageUrl: "https://i.imgur.com/yXOvdOSs.jpg",
  imageSize: 90
};

export default function Profile() {
  return (
    <>
      <h1>{user.name}</h1>
      <img
        className="avatar"
        src={user.imageUrl}
        alt={"Photo of " + user.name}
        style={{
          width: user.imageSize,
          height: user.imageSize
        }}
      />
    </>
  );
}
```

上の例では、`style={{}}` は特殊な構文ではなく、`style={ }` の JSX の波括弧の中の通常の `{}` オブジェクトです。スタイルが JavaScript 変数に依存する場合、`style` 属性を使用できます。
