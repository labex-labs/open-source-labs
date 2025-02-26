# React useBodyScrollLock フック

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

このコード スニペットを使うと、モーダルが開いているときに body のスクロールをロックできます。その仕組みは次の通りです。

まず、`useBodyScrollLock` 関数が定義されており、これは `useLayoutEffect` フックを使って `body` 要素のスクロールをロックします。このフックはコンポーネントがマウントされたときに一度だけ実行され、`body` 要素の `overflow` 値を `'hidden'` に設定します。コンポーネントがアンマウントされるときには、元の `overflow` 値が復元されます。

```jsx
const useBodyScrollLock = () => {
  React.useLayoutEffect(() => {
    const originalStyle = window.getComputedStyle(document.body).overflow;
    document.body.style.overflow = "hidden";
    return () => (document.body.style.overflow = originalStyle);
  }, []);
};
```

次に、`Modal` コンポーネントが定義されており、これは `useBodyScrollLock` 関数を利用しています。このコンポーネントは画面中央に表示されるボックス内にメッセージを表示します。ボックスをクリックすると、モーダルが閉じられ、body のスクロールが解除されます。

```jsx
const Modal = ({ onClose }) => {
  useBodyScrollLock();

  return (
    <div
      style={{
        zIndex: 100,
        background: "rgba(0,0,0,0.25)",
        display: "flex",
        justifyContent: "center",
        alignItems: "center"
      }}
      onClick={onClose}
    >
      <p style={{ padding: 8, borderRadius: 8, background: "#fff" }}>
        Scroll locked! <br /> Click me to unlock
      </p>
    </div>
  );
};
```

最後に、`MyApp` コンポーネントが定義されており、これはクリックすると `Modal` コンポーネントを開くボタンをレンダリングします。

```jsx
const MyApp = () => {
  const [modalOpen, setModalOpen] = React.useState(false);

  return (
    <div
      style={{
        height: "400vh",
        textAlign: "center",
        paddingTop: 100,
        background: "linear-gradient(to bottom, #1fa2ff, #12d8fa, #a6ffcb)"
      }}
    >
      <button onClick={() => setModalOpen(true)}>Open modal</button>
      {modalOpen && <Modal onClose={() => setModalOpen(false)} />}
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

右下隅の「Go Live」をクリックして 8080 番ポートでウェブ サービスを実行してください。その後、**Web 8080** タブを更新してウェブ ページをプレビューできます。
