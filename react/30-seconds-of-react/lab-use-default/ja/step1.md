# React useDefaultフック

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

以下がコードです。

```jsx
const useDefault = (defaultState, initialState) => {
  const [value, setValue] = React.useState(initialState);
  const isEmpty = value === undefined || value === null;
  return [isEmpty ? defaultState : value, setValue];
};
```

```jsx
const UserCard = () => {
  const [user, setUser] = useDefault({ name: "Adam" }, { name: "John" });

  return (
    <>
      <div>User: {user.name}</div>
      <input onChange={(e) => setUser({ name: e.target.value })} />
      <button onClick={() => setUser(null)}>Clear</button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<UserCard />);
```

デフォルトのフォールバック付きの状態付きの値を作成するには、React の `useState()` フックを使用します。初期値が `null` または `undefined` であるかどうかを確認します。そうであれば代わりに `defaultState` を返し、そうでなければ実際の `value` 状態と `setValue` 関数を返します。上記のコードは、`useDefault` と呼ばれるカスタムフックでこの機能を実装する方法を示しています。

提供された例では、`useDefault` を使用してデフォルト値 `{ name: 'Adam' }` で `user` 状態を作成しています。初期状態は `{ name: 'John' }` に設定されています。`UserCard` コンポーネントでは、`user` とその名前を更新する入力フィールドが表示されます。また、状態を `null` にリセットするクリアボタンも用意されています。最後に、`ReactDOM.createRoot()` を使用してコンポーネントをレンダリングします。

右下隅の「Go Live」をクリックして、ポート8080でウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
