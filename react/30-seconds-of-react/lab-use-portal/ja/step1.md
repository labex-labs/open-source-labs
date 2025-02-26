# React usePortal フック

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

親コンポーネントの外で子コンポーネントをレンダリングするポータルを作成するには、次の手順に従います。

1. `useState()` フックを使用して、ポータルの `render()` と `remove()` 関数を保持する状態変数を作成します。
2. `ReactDOM.createPortal()` と `ReactDOM.unmountComponentAtNode()` を使用して、ポータルとそれを削除する関数を作成します。`useCallback()` フックを使用して、これらの関数を `createPortal()` としてラップしてメモ化します。
3. `useEffect()` フックを使用して、`el` の値が変更されるたびに `createPortal()` を呼び出し、状態変数を更新します。
4. 最後に、状態変数の `render()` 関数を返します。

以下は、例としての実装です。

```jsx
const usePortal = (el) => {
  const [portal, setPortal] = React.useState({
    render: () => null,
    remove: () => null
  });

  const createPortal = React.useCallback((el) => {
    const Portal = ({ children }) => ReactDOM.createPortal(children, el);
    const remove = () => ReactDOM.unmountComponentAtNode(el);
    return { render: Portal, remove };
  }, []);

  React.useEffect(() => {
    if (el) portal.remove();
    const newPortal = createPortal(el);
    setPortal(newPortal);
    return () => newPortal.remove(el);
  }, [el]);

  return portal.render;
};
```

このフックを使用するには、必要な DOM 要素を引数として `usePortal()` を呼び出すコンポーネントを作成します。このコンポーネントは、返された `render()` 関数を使用して、ポータル内にコンテンツをレンダリングできます。

```jsx
const App = () => {
  const Portal = usePortal(document.querySelector("title"));

  return (
    <p>
      Hello world!
      <Portal>Portalized Title</Portal>
    </p>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新して、ウェブページをプレビューできます。
