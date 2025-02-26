# React useEventListener フック

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

この関数は、指定された要素に対して指定されたイベントタイプのイベントリスナーを追加します。この関数を使用するには、次の手順に従います。

1. `handler` を保持するための ref を作成するために `useRef()` フックを使用します。
2. `handler` が変更されるたびに、`savedHandler` ref の値を更新するために `useEffect()` フックを使用します。
3. 与えられた要素にイベントリスナーを追加し、マウント解除時にクリーンアップするために `useEffect()` フックを使用します。
4. 最後の引数 `el` を省略することで、既定で `Window` を使用します。

以下がコードです。

```jsx
const useEventListener = (type, handler, el = window) => {
  const savedHandler = React.useRef(handler);

  React.useEffect(() => {
    savedHandler.current = handler;
  }, [handler]);

  React.useEffect(() => {
    const listener = (e) => savedHandler.current(e);

    el.addEventListener(type, listener);

    return () => {
      el.removeEventListener(type, listener);
    };
  }, [type, el]);
};
```

そして、`useEventListener()` 関数の使用例を以下に示します。

```jsx
const MyApp = () => {
  const [coords, setCoords] = React.useState({ x: 0, y: 0 });

  const updateCoords = React.useCallback(
    ({ clientX, clientY }) => {
      setCoords({ x: clientX, y: clientY });
    },
    [setCoords]
  );

  useEventListener("mousemove", updateCoords);

  return (
    <p>
      Mouse coordinates: {coords.x}, {coords.y}
    </p>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新して、ウェブページをプレビューできます。
