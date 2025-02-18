# 波紋エフェクト付きボタン

> `index.html` と `script.js` はすでに仮想マシン（VM）に用意されています。一般的には、`script.js` と `style.css` にコードを追加するだけです。

このコードは、クリックされたときに波紋エフェクトを生成するボタンコンポーネントをレンダリングします。動作原理は以下の通りです。

- `useState()` フックを使用して、2 つの状態変数 `coords` と `isRippling` を作成します。`coords` 変数はポインタの座標を格納し、`isRippling` はボタンのアニメーション状態を格納します。
- `useEffect()` フックを使用して、`coords` 状態変数が変更されるたびに `isRippling` の値を変更します。これにより、波紋エフェクトのアニメーションが開始されます。
- 前のフックで `setTimeout()` を使用して、アニメーションの再生が終了した後にアニメーションをクリアします。
- 別の `useEffect()` フックを使用して、`isRippling` 状態変数が `false` のときに `coords` をリセットします。
- `onClick` イベントは、`coords` 状態変数を更新し、渡されたコールバック関数を呼び出すことで処理されます。

以下は `RippleButton` コンポーネントのコードです。

```jsx
const RippleButton = ({ children, onClick }) => {
  const [coords, setCoords] = React.useState({ x: -1, y: -1 });
  const [isRippling, setIsRippling] = React.useState(false);

  React.useEffect(() => {
    if (coords.x !== -1 && coords.y !== -1) {
      setIsRippling(true);
      setTimeout(() => setIsRippling(false), 300);
    } else setIsRippling(false);
  }, [coords]);

  React.useEffect(() => {
    if (!isRippling) setCoords({ x: -1, y: -1 });
  }, [isRippling]);

  return (
    <button
      className="ripple-button"
      onClick={(e) => {
        const rect = e.target.getBoundingClientRect();
        setCoords({ x: e.clientX - rect.left, y: e.clientY - rect.top });
        onClick && onClick(e);
      }}
    >
      {isRippling && (
        <span
          className="ripple"
          style={{
            left: coords.x,
            top: coords.y
          }}
        />
      )}
      <span className="content">{children}</span>
    </button>
  );
};
```

このコンポーネントは以下のように使用できます。

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <RippleButton onClick={(e) => console.log(e)}>Click me</RippleButton>
);
```

以下は `RippleButton` コンポーネントの CSS です。

```css
.ripple-button {
  border-radius: 4px;
  border: none;
  margin: 8px;
  padding: 14px 24px;
  background: #1976d2;
  color: #fff;
  overflow: hidden;
  position: relative;
  cursor: pointer;
}

.ripple-button > .ripple {
  width: 20px;
  height: 20px;
  position: absolute;
  background: #63a4ff;
  display: block;
  content: "";
  border-radius: 9999px;
  opacity: 1;
  animation: 0.9s ease 1 forwards ripple-effect;
}

@keyframes ripple-effect {
  0% {
    transform: scale(1);
    opacity: 1;
  }
  50% {
    transform: scale(10);
    opacity: 0.375;
  }
  100% {
    transform: scale(35);
    opacity: 0;
  }
}

.ripple-button > .content {
  position: relative;
  z-index: 2;
}
```

右下隅にある「Go Live」をクリックして、ポート 8080 で Web サービスを実行してください。その後、**Web 8080** タブを更新すると、Web ページをプレビューできます。
