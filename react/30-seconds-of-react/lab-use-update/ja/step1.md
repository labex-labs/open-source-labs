# React useUpdate フック

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

コンポーネントを呼び出したときに再レンダリングさせるには、`useReducer()` フックを使用して、更新されるたびに新しいオブジェクトを作成し、そのディスパッチを返します。以下は `useUpdate()` 関数の例としての実装です：

```jsx
const useUpdate = () => {
  const [, update] = React.useReducer(() => ({}));
  return update;
};
```

その後、必要に応じてコンポーネントで `useUpdate()` を使用して再レンダリングをトリガーすることができます：

```jsx
const MyApp = () => {
  const update = useUpdate();

  return (
    <>
      <div>Time: {Date.now()}</div>
      <button onClick={update}>Update</button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新して、ウェブページをプレビューすることができます。
