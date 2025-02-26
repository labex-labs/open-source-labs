# パスワードの表示/非表示トグル

> VM内には既に`index.html`と`script.js`が用意されています。一般的には、`script.js`と`style.css`にのみコードを追加すればよいです。

次のコードは、表示ボタン付きのパスワード入力フィールドをレンダリングします。`useState()`フックを使って`shown`という状態変数を作成し、その初期値を`false`に設定しています。「表示/非表示」ボタンがクリックされると、`setShown`関数が呼び出され、入力の`type`が`'text'`と`'password'`の間で切り替わります。

```jsx
const PasswordRevealer = ({ value }) => {
  const [shown, setShown] = React.useState(false);
  return (
    <>
      <input type={shown ? "text" : "password"} value={value} />
      <button onClick={() => setShown(!shown)}>Show/Hide</button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <PasswordRevealer />
);
```

右下隅の「Go Live」をクリックして、ポート8080でウェブサービスを実行してください。その後、**Web 8080**タブを更新して、ウェブページをプレビューできます。
