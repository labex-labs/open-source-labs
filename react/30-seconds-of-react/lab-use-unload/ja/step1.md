# React の useUnload フック

> `index.html` と `script.js` はすでに仮想マシン（VM）に用意されています。一般的には、`script.js` と `style.css` にコードを追加するだけです。

`beforeunload` ウィンドウイベントは、以下の手順で処理できます。

1. `useRef()` フックを使用して、コールバック関数 `fn` のリフ（ref）を作成します。
2. `useEffect()` フックと `EventTarget.addEventListener()` を使用して、ユーザーがウィンドウを閉じようとしたときにトリガーされる `'beforeunload'` イベントを処理します。
3. `EventTarget.removeEventListener()` を使用して、コンポーネントがアンマウントされた後のクリーンアップを行います。

コードは次の通りです。

```jsx
const useUnload = (fn) => {
  const callbackRef = React.useRef(fn);

  React.useEffect(() => {
    const callback = callbackRef.current;
    window.addEventListener("beforeunload", callback);
    return () => {
      window.removeEventListener("beforeunload", callback);
    };
  }, [callbackRef]);
};

const App = () => {
  useUnload((e) => {
    e.preventDefault();
    const exit = confirm("Are you sure you want to leave?");
    if (exit) window.close();
  });

  return <div>Try closing the window.</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

右下隅にある「Go Live」をクリックして、ポート 8080 で Web サービスを実行してください。その後、**Web 8080** タブを更新すると、Web ページをプレビューできます。
