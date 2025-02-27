# 画面の更新

> VM 内には既に React プロジェクトが用意されています。一般的には、`App.js` にコードを追加するだけです。

依存関係をインストールするには、次のコマンドを使用してください。

```bash
npm i
```

多くの場合、コンポーネントにはいくつかの情報を「保持」して表示する必要があります。たとえば、ボタンがクリックされた回数を数えたい場合があります。これを行うには、コンポーネントに状態を追加します。

まず、React から `useState` をインポートします。

```js
import { useState } from "react";
```

これで、コンポーネント内で状態変数を宣言できます。

```js
function MyButton() {
  const [count, setCount] = useState(0);
  //...
```

`useState` からは 2 つのものが得られます。現在の状態 (`count`) と、それを更新するための関数 (`setCount`) です。名前は何でも良いですが、慣例として `[何か, set何か]` と書きます。

ボタンが最初に表示されたとき、`count` は `0` になります。なぜなら、`useState()` に `0` を渡したからです。状態を変更したいときは、`setCount()` を呼び出して新しい値を渡します。このボタンをクリックすると、カウンターがインクリメントされます。

```js
function MyButton() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return <button onClick={handleClick}>Clicked {count} times</button>;
}
```

React は再度コンポーネント関数を呼び出します。今回は、`count` が `1` になります。次は `2` になります。以下同様です。

同じコンポーネントを複数回レンダリングすると、それぞれが独自の状態を持ちます。それぞれのボタンを個別にクリックしてみてください。

```js
// App.js
import { useState } from "react";

export default function MyApp() {
  return (
    <div>
      <h1>Counters that update separately</h1>
      <MyButton />
      <MyButton />
    </div>
  );
}

function MyButton() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return <button onClick={handleClick}>Clicked {count} times</button>;
}
```

それぞれのボタンが独自の `count` 状態を「保持」し、他のボタンに影響を与えないことに注目してください。

プロジェクトを実行するには、次のコマンドを使用します。その後、**Web 8080** タブを更新して Web ページをプレビューできます。

```bash
npm start
```
