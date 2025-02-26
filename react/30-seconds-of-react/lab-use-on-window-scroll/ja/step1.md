# React useOnWindowScroll フック

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

この関数は、ウィンドウがスクロールされるたびにコールバック関数を実行します。それを実装するには：

1. `useRef()` フックを使用して参照変数 `listener` を作成します。
2. `useEffect()` フックと `EventTarget.addEventListener()` を使用して、`Window` オブジェクトの `'scroll'` イベントをリッスンし、リスナー参照を `listener.current` に割り当てます。
3. コンポーネントがアンマウントされたときに、既存のリスナーを削除するために `EventTarget.removeEventListener()` を使用します。

以下がコードです：

```jsx
const useOnWindowScroll = (callback) => {
  const listener = React.useRef(null);

  React.useEffect(() => {
    if (listener.current) {
      window.removeEventListener("scroll", listener.current);
    }
    listener.current = () => {
      callback(window.pageYOffset);
    };
    window.addEventListener("scroll", listener.current);
    return () => {
      window.removeEventListener("scroll", listener.current);
    };
  }, [callback]);
};
```

この関数をテストするには、次のようにコンポーネントで使用できます：

```jsx
const App = () => {
  useOnWindowScroll((scrollY) => console.log(`scroll Y: ${scrollY}`));
  return <p style={{ height: "300vh" }}>Scroll and check the console</p>;
};

ReactDOM.render(<App />, document.getElementById("root"));
```

これにより、ウィンドウがスクロールされるたびに、ウィンドウの垂直方向のスクロール位置がコンソールにログ表示されます。

右下隅の「Go Live」をクリックして、ポート 8080 でウェブ サービスを実行してください。その後、**Web 8080** タブを更新して、ウェブ ページをプレビューできます。
