# React useTimeout フック

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

宣言的に `setTimeout()` を実装するには、`callback` と `delay` を受け取るカスタムフックを作成します。`useRef()` フックを使ってコールバック関数用の `ref` を作成し、`useEffect()` フックを使って最新のコールバックを覚えておきます。そして、`useEffect()` フックを使ってタイムアウトを設定してクリーンアップします。

このアプローチを示すコードのサンプルは次の通りです。

```jsx
const useTimeout = (callback, delay) => {
  const savedCallback = React.useRef();

  React.useEffect(() => {
    savedCallback.current = callback;
  }, [callback]);

  React.useEffect(() => {
    const tick = () => {
      savedCallback.current();
    };
    if (delay !== null) {
      let id = setTimeout(tick, delay);
      return () => clearTimeout(id);
    }
  }, [delay]);
};

const OneSecondTimer = (props) => {
  const [seconds, setSeconds] = React.useState(0);

  useTimeout(() => {
    setSeconds(seconds + 1);
  }, 1000);

  return <p>{seconds}</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<OneSecondTimer />);
```

右下隅の「Go Live」をクリックして 8080 ポートでウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
