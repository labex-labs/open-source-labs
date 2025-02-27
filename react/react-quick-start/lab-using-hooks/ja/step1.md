# フックの使用

> VM には既に React プロジェクトが用意されています。一般的には、`App.js` にコードを追加するだけです。

依存関係をインストールするには、次のコマンドを使用してください。

```bash
npm i
```

`use` で始まる関数はフックと呼ばれます。`useState` は React によって提供される組み込みフックです。API リファレンスで他の組み込みフックを見つけることもできます。既存のフックを組み合わせて独自のフックを書くこともできます。

フックは他の関数よりも制限が多くなっています。フックを呼び出すことができるのは、コンポーネントの一番上（または他のフックの一番上）だけです。条件分岐やループの中で `useState` を使いたい場合は、新しいコンポーネントを抽出してそこに置きます。

前の例では、各 `MyButton` が独自の独立した `count` を持ち、各ボタンがクリックされると、クリックされたボタンの `count` だけが変更されました。

![フックを使用していない](../assets/1.png)

しかし、多くの場合、コンポーネントがデータを共有し、常に一緒に更新される必要があります。

両方の `MyButton` コンポーネントが同じ `count` を表示し、一緒に更新するには、個々のボタンの状態を「上に」移動して、それらを含む最も近いコンポーネントにする必要があります。

この例では、`MyApp` です。

![フックを使用している](../assets/2.png)

今、どちらのボタンをクリックしても、`MyApp` 内の `count` が変更され、それにより `MyButton` 内の両方の `count` が変更されます。これをコードで表現する方法は次の通りです。

まず、状態を `MyButton` から `MyApp` に上げます。

```js
// App.js
export default function MyApp() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <div>
      <h1>Counters that update separately</h1>
      <MyButton />
      <MyButton />
    </div>
  );
}

function MyButton() {
  //... ここからコードを移動しています...
}
```

次に、共有されたクリックハンドラとともに、状態を `MyApp` から各 `MyButton` に渡します。`<img>` のような既存のタグと同じように、JSX の波括弧を使って `MyButton` に情報を渡すことができます。

```js
export default function MyApp() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <div>
      <h1>Counters that update together</h1>
      <MyButton count={count} onClick={handleClick} />
      <MyButton count={count} onClick={handleClick} />
    </div>
  );
}
```

このように渡す情報は `props` と呼ばれます。今、`MyApp` コンポーネントには `count` 状態と `handleClick` イベントハンドラが含まれ、それらの両方を `props` として各ボタンに渡しています。

最後に、`MyButton` を変更して、親コンポーネントから渡された `props` を読み取るようにします。

```js
function MyButton({ count, onClick }) {
  return <button onClick={onClick}>Clicked {count} times</button>;
}
```

ボタンをクリックすると、`onClick` ハンドラが実行されます。各ボタンの `onClick` `props` は `MyApp` 内の `handleClick` 関数に設定されているため、その中のコードが実行されます。そのコードは `setCount(count + 1)` を呼び出し、`count` 状態変数をインクリメントします。新しい `count` 値が各ボタンに `props` として渡されるため、すべてが新しい値を表示します。これは「状態を上げる」と呼ばれます。状態を上げることで、コンポーネント間で共有することができます。

```js
import { useState } from "react";

export default function MyApp() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <div>
      <h1>Counters that update together</h1>
      <MyButton count={count} onClick={handleClick} />
      <MyButton count={count} onClick={handleClick} />
    </div>
  );
}

function MyButton({ count, onClick }) {
  return <button onClick={onClick}>Clicked {count} times</button>;
}
```

プロジェクトを実行するには、次のコマンドを使用してください。その後、**Web 8080** タブを更新して Web ページをプレビューできます。

```bash
npm start
```
