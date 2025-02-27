# イベントに応答する

> VM には既に React プロジェクトが用意されています。一般的には、`App.js` にコードを追加するだけです。

依存関係をインストールするには、次のコマンドを使用してください。

```bash
npm i
```

React を使うと、JSX にイベントハンドラを追加できます。イベントハンドラは、クリック、ホバー、フォーム入力へのフォーカスなどのインタラクションに応答してトリガーされる自分自身の関数です。

イベントハンドラを追加するには、まず関数を定義してから、それを適切な JSX タグに [prop として渡します](https://react.dev/learn/passing-props-to-a-component)。たとえば、まだ何もしないボタンは次のようになります。

```js
// App.js
export default function Button() {
  return <button>I don't do anything</button>;
}
```

ユーザーがクリックしたときにメッセージを表示するには、次の 3 つの手順に従います。

1. `Button` コンポーネント内に `handleClick` と呼ばれる関数を宣言します。
2. その関数内のロジックを実装します（メッセージを表示するために `alert` を使用します）。
3. `<button>` JSX に `onClick={handleClick}` を追加します。

```js
export default function Button() {
  function handleClick() {
    alert("You clicked me!");
  }

  return <button onClick={handleClick}>Click me</button>;
}
```

`handleClick` 関数を定義してから、それを `<button>` に prop として渡しました。`handleClick` はイベントハンドラです。イベントハンドラ関数は：

通常、コンポーネント内で定義されます。
名前が `handle` で始まり、その後にイベント名が続きます。

プロジェクトを実行するには、次のコマンドを使用してください。その後、**Web 8080** タブを更新して Web ページをプレビューできます。

```bash
npm start
```

慣例として、イベントハンドラの名前は `handle` の後にイベント名が続くように命名されます。よく見るのは `onClick={handleClick}`、`onMouseEnter={handleMouseEnter}` などです。

あるいは、JSX 内でイベントハンドラをインラインで定義することもできます。

```js
<button onClick={function handleClick() {
  alert('You clicked me!');
}}>
```

あるいは、より簡潔に、アロー関数を使って：

```js
<button onClick={() => {
  alert('You clicked me!');
}}>
```

これらのスタイルはすべて同等です。インラインイベントハンドラは短い関数に便利です。
