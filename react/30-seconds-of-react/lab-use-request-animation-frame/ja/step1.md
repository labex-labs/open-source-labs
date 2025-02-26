# React useRequestAnimationFrame フック

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

各再描画の前にアニメーション関数を実行するには、`useRef()` フックを使って `requestRef` と `previousTimeRef` 変数を作成します。その後、これらの変数を更新し、`callback` を実行し、永続的に `Window.requestAnimationFrame()` を呼び出す `animate()` 関数を定義します。最後に、空の配列を使って `useEffect()` フックを使って、`requestRef` の値を `Window.requestAnimationFrame()` で初期化し、コンポーネントがアンマウントされたときに返される値と `Window.cancelAnimationFrame()` を使ってクリーンアップします。

以下は `useRequestAnimationFrame()` の例の実装です：

```jsx
const useRequestAnimationFrame = (callback) => {
  const requestRef = React.useRef();
  const previousTimeRef = React.useRef();

  const animate = (time) => {
    if (previousTimeRef.current) {
      callback(time - previousTimeRef.current);
    }
    previousTimeRef.current = time;
    requestRef.current = requestAnimationFrame(animate);
  };

  React.useEffect(() => {
    requestRef.current = requestAnimationFrame(animate);
    return () => cancelAnimationFrame(requestRef.current);
  }, []);
};
```

このカスタムフックをコンポーネントで使用するには、単にコールバック関数を渡します。たとえば、100 FPS で更新される単純なカウンターを作成するには：

```jsx
const Counter = () => {
  const [count, setCount] = React.useState(0);

  useRequestAnimationFrame((deltaTime) => {
    setCount((prevCount) => (prevCount + deltaTime * 0.01) % 100);
  });

  return <p>{Math.round(count)}</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Counter />);
```

右下隅の「Go Live」をクリックして、ポート 8080 で Web サービスを実行してください。その後、**Web 8080** タブを更新して Web ページをプレビューできます。
