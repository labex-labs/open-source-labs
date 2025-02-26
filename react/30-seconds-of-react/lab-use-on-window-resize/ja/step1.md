# React useOnWindowResizeフック

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

このコードは、ウィンドウがリサイズされるたびにコールバック関数を実行します。それを実装するには、次の手順に従ってください。

1. `useRef()` フックを使用して `listener` と呼ばれる変数を作成します。この変数は、リスナーへの参照を格納します。
2. `useEffect()` フックと `EventTarget.addEventListener()` を使用して、`Window` グローバルオブジェクトの `'resize'` イベントをリッスンします。イベントがトリガーされたときに、`callback` 関数を呼び出します。
3. コンポーネントがアンマウントされたときに、`EventTarget.removeEventListener()` を使用して既存のリスナーを削除することでクリーンアップします。

以下がコードです。

```jsx
const useOnWindowResize = (callback) => {
  const listener = React.useRef(null);

  React.useEffect(() => {
    if (listener.current) {
      window.removeEventListener("resize", listener.current);
    }
    listener.current = callback;
    window.addEventListener("resize", callback);
    return () => {
      window.removeEventListener("resize", callback);
    };
  }, [callback]);
};

const App = () => {
  useOnWindowResize(() =>
    console.log(`Window size: (${window.innerWidth}, ${window.innerHeight})`)
  );
  return <p>Resize the window and check the console.</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

右下隅の「Go Live」をクリックして、ポート8080でウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
