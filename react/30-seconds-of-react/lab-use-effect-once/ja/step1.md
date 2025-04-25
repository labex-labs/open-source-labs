# React useEffectOnce フック

> VM 内には既に`index.html`と`script.js`が用意されています。一般的には、`script.js`と`style.css`にのみコードを追加すればよいです。

以下のコードは、`when`条件が真になったときに`callback`を 1 回だけ実行する関数`useEffectOnce(callback, when)`を実装しています。

この関数を実装するには：

- `useRef()`フックを使用して、エフェクトの実行状態を追跡するための変数`hasRunOnce`を作成します。
- `when`条件が変更されたときにのみ実行される`useEffect()`フックを使用します。
- `useEffect()`フックの中で、`when`が`true`で、かつエフェクトが以前に実行されていないことを確認します。両方が`true`の場合、`callback`を実行して、`hasRunOnce`を`true`に設定します。

```jsx
const useEffectOnce = (callback, when) => {
  const hasRunOnce = React.useRef(false);
  React.useEffect(() => {
    if (when && !hasRunOnce.current) {
      callback();
      hasRunOnce.current = true;
    }
  }, [when]);
};
```

ここに`useEffectOnce()`の使用例を示します：

```jsx
const App = () => {
  const [clicked, setClicked] = React.useState(false);
  useEffectOnce(() => {
    console.log("mounted");
  }, clicked);
  return <button onClick={() => setClicked(true)}>Click me</button>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

この例では、`useEffectOnce()`はボタンが初めてクリックされたときにコンソールに「mounted」とログを出力するために使用されています。`useEffectOnce()`フックには 2 つの引数が渡されます：実行する`callback`とチェックする`when`条件です。`when`条件は`clicked`状態に設定されているため、`callback`は`clicked`が初めて`true`になったときにのみ実行されます。

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080**タブを更新して、ウェブページをプレビューできます。
