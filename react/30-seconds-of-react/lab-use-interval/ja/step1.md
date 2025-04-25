# React useInterval フック

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

宣言的な方法で `setInterval()` を実装するには、`callback` と `delay` を受け取るカスタムフックを作成できます。最初のステップは、`useRef()` フックを使ってコールバック関数用の `ref` を作成することです。次に、`useEffect()` フックを使って、`callback` が変更されるたびに最新の `callback` を记忆します。最后に、`delay` に依存する `useEffect()` フックを使ってインターバルを设定してクリーンアップします。

ここに、カスタムフックのコードスニペットの例を示します。

```jsx
const useInterval = (callback, delay) => {
  const savedCallback = React.useRef();

  React.useEffect(() => {
    savedCallback.current = callback;
  }, [callback]);

  React.useEffect(() => {
    const tick = () => {
      savedCallback.current();
    };
    if (delay !== null) {
      let id = setInterval(tick, delay);
      return () => clearInterval(id);
    }
  }, [delay]);
};
```

次に、このカスタムフックをコンポーネントで使用できます。たとえば、1 秒ごとに更新されるタイマーを作成するには：

```jsx
const Timer = (props) => {
  const [seconds, setSeconds] = React.useState(0);

  useInterval(() => {
    setSeconds(seconds + 1);
  }, 1000);

  return <p>{seconds}</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Timer />);
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
