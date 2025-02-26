# React useOnGlobalEvent フック

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

この関数は、グローバル オブジェクトでイベントが発生するたびにコールバック関数を実行します。この関数を実装するには：

1. `useRef()` フックを使って、リスナーの参照を保持する変数 `listener` を作成します。
2. `type` と `options` 引数の前回の値を保持する変数を `useRef()` フックを使って作成します。
3. `useEffect()` フックと `EventTarget.addEventListener()` を使って、`Window` グローバル オブジェクトで指定されたイベント `type` をリッスンします。
4. `EventTarget.removeEventListener()` を使って、既存のリスナーを削除し、コンポーネントがアンマウントされたときにクリーンアップします。

```jsx
const useOnGlobalEvent = (type, callback, options) => {
  const listener = React.useRef(null);
  const previousProps = React.useRef({ type, options });

  React.useEffect(() => {
    const { type: previousType, options: previousOptions } =
      previousProps.current;

    if (listener.current) {
      window.removeEventListener(
        previousType,
        listener.current,
        previousOptions
      );
    }

    listener.current = callback;
    window.addEventListener(type, callback, options);
    previousProps.current = { type, options };

    return () => {
      window.removeEventListener(type, listener.current, options);
    };
  }, [callback, type, options]);
};
```

この関数の使い方の例を以下に示します：

```jsx
const App = () => {
  useOnGlobalEvent("mousemove", (e) => {
    console.log(`(${e.x}, ${e.y})`);
  });

  return <p>Move your mouse around</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブ サービスを実行してください。その後、**Web 8080** タブを更新してウェブ ページをプレビューできます。
