# React useWindowSize フック

> VM には既に `index.html` と `script.js` が提供されています。一般的には、`script.js` と `style.css` にのみコードを追加する必要があります。

ブラウザウィンドウの寸法を追跡するには、次の手順を踏みます。

1. `useState()` フックを使用して、ウィンドウの寸法を保持する状態変数 `windowSize` を初期化します。サーバーレンダリングとクライアントレンダリングの間の不一致を回避するため、両方の値を `undefined` に設定して初期化します。

```jsx
const [windowSize, setWindowSize] = React.useState({
  width: undefined,
  height: undefined
});
```

2. `Window.innerWidth` と `Window.innerHeight` を使用して状態変数を更新する関数 `handleResize()` を作成します。この関数は、`'resize'` イベントがトリガーされるたびに呼び出されます。

```jsx
const handleResize = () =>
  setWindowSize({ width: window.innerWidth, height: window.innerHeight });
```

3. `useEffect()` フックを使用して、マウント時に `'resize'` イベントに適切なリスナーを設定し、アンマウント時にそれをクリーンアップします。

```jsx
React.useEffect(() => {
  window.addEventListener("resize", handleResize);

  handleResize();

  return () => {
    window.removeEventListener("resize", handleResize);
  };
}, []);
```

これらをまとめると、`useWindowSize()` カスタムフックは次のように定義できます。

```jsx
const useWindowSize = () => {
  const [windowSize, setWindowSize] = React.useState({
    width: undefined,
    height: undefined
  });

  const handleResize = () =>
    setWindowSize({ width: window.innerWidth, height: window.innerHeight });

  React.useEffect(() => {
    window.addEventListener("resize", handleResize);

    handleResize();

    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []);

  return windowSize;
};
```

`useWindowSize()` フックを使用するには、コンポーネント内で単にそれを呼び出し、返されたオブジェクトから `width` と `height` の値を分解します。

```jsx
const MyApp = () => {
  const { width, height } = useWindowSize();

  return (
    <p>
      Window size: ({width} x {height})
    </p>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
