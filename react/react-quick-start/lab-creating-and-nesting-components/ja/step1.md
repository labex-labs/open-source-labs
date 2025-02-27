# コンポーネントの作成とネスト

> VM には既に React プロジェクトが用意されています。一般的には、`App.js` にコードを追加するだけです。

依存関係をインストールするには、次のコマンドを使用してください。

```bash
npm i
```

React アプリケーションはコンポーネントで構成されています。コンポーネントは独自のロジックと外観を持つ UI（ユーザーインターフェイス）の一部です。コンポーネントはボタンほど小さくても、ページ全体ほど大きくても構いません。

React コンポーネントはマークアップを返す JavaScript 関数です。

```js
// App.js
function MyButton() {
  return <button>I'm a button</button>;
}
```

`MyButton` を宣言したので、別のコンポーネントにネストすることができます。

```js
// App.js
export default function MyApp() {
  return (
    <div>
      <h1>Welcome to my app</h1>
      <MyButton />
    </div>
  );
}
```

`<MyButton />` が大文字で始まることに注意してください。これが React コンポーネントであることを示しています。React コンポーネント名は常に大文字で始める必要があり、HTML タグは小文字でなければなりません。

`export default` キーワードは、ファイル内のメインコンポーネントを指定します。JavaScript の構文に慣れていない場合は、[MDN](https://developer.mozilla.org/en-US/docs/web/javascript/reference/statements/export) と [javascript.info](https://javascript.info/import-export) に素晴らしいリファレンスがあります。

プロジェクトを実行するには、次のコマンドを使用してください。その後、**Web 8080** タブを更新して Web ページをプレビューできます。

```bash
npm start
```
