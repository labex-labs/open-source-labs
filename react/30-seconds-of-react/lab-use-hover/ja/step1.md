# React useHoverフック

> VM内には既に`index.html`と`script.js`が用意されています。一般的には、`script.js`と`style.css`にのみコードを追加すればよいです。

このコードは、ラップされたコンポーネントにマウスオーバーするイベントを処理するカスタムフックを作成します。

このフックを使用するには：

- `useState()`を使用して、マウスオーバー状態を保持する変数を作成します。
- `useCallback()`を使用して、状態を更新する2つのハンドラ関数をメモ化します。
- `useCallback()`を使用して、コールバックリフを作成し、`'mouseover'`と`'mouseout'`イベントのリスナーを作成または更新します。
- `useRef()`を使用して、最後に`callbackRef`に渡されたノードを追跡し、そのリスナーを削除できるようにします。

```jsx
const useHover = () => {
  const [isHovering, setIsHovering] = React.useState(false);
  const handleMouseOver = React.useCallback(() => setIsHovering(true), []);
  const handleMouseOut = React.useCallback(() => setIsHovering(false), []);
  const nodeRef = React.useRef();
  const callbackRef = React.useCallback(
    (node) => {
      if (nodeRef.current) {
        nodeRef.current.removeEventListener("mouseover", handleMouseOver);
        nodeRef.current.removeEventListener("mouseout", handleMouseOut);
      }
      nodeRef.current = node;
      if (nodeRef.current) {
        nodeRef.current.addEventListener("mouseover", handleMouseOver);
        nodeRef.current.addEventListener("mouseout", handleMouseOut);
      }
    },
    [handleMouseOver, handleMouseOut]
  );

  return [callbackRef, isHovering];
};
```

これは、このフックの使用例です：

```jsx
const MyApp = () => {
  const [hoverRef, isHovering] = useHover();
  return <div ref={hoverRef}>{isHovering ? "Hovering" : "Not hovering"}</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

右下隅の「Go Live」をクリックして、ポート8080でWebサービスを実行してください。その後、**Web 8080**タブを更新してWebページをプレビューできます。
