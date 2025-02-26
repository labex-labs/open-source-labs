# React useSSR フック

> VM 内には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

コードがブラウザ上で実行されているか、サーバ上で実行されているかを確認するには、`typeof`、`Window`、`Window.document`、`Document.createElement()` を使って DOM が利用可能かどうかを判定するカスタムフックを作成します。`useState()` フックを使って `inBrowser` という状態変数を定義し、`useEffect()` フックを使ってそれを更新し、最後にクリーンアップします。カスタムフックの返却値をメモ化するには `useMemo()` フックを使います。

以下がコードです。

```jsx
const isDOMavailable = !!(
  typeof window !== "undefined" &&
  window.document &&
  window.document.createElement
);

const useSSR = () => {
  const [inBrowser, setInBrowser] = React.useState(isDOMavailable);

  React.useEffect(() => {
    setInBrowser(isDOMavailable);
    return () => {
      setInBrowser(false);
    };
  }, []);

  const useSSRObject = React.useMemo(
    () => ({
      isBrowser: inBrowser,
      isServer: !inBrowser,
      canUseWorkers: typeof Worker !== "undefined",
      canUseEventListeners: inBrowser && !!window.addEventListener,
      canUseViewport: inBrowser && !!window.screen
    }),
    [inBrowser]
  );

  return useSSRObject;
};

const SSRChecker = (props) => {
  const { isBrowser, isServer } = useSSR();

  return <p>{isBrowser ? "Running on browser" : "Running on server"}</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<SSRChecker />);
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
