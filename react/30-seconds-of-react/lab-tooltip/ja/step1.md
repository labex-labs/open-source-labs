# ツールチップ

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

以下は、もっと明確で簡潔で整合性のあるバージョンのコンテンツです。

---

このコードはツールチップコンポーネントを作成します。これを使用するには、以下の手順を実行します。

1. `useState()` フックを使用して `show` 変数を作成し、`false` に設定します。
2. ツールチップ要素とコンポーネントに渡された `children` を含むコンテナ要素をレンダリングします。
3. `show` 変数によって制御されるツールチップの `className` を切り替えることで、`onMouseEnter` と `onMouseLeave` イベントを処理します。

以下はツールチップコンポーネントのコードです。

```css
.tooltip-container {
  position: relative;
}

.tooltip-box {
  position: absolute;
  top: calc(100% + 5px);
  display: none;
  padding: 5px;
  border-radius: 5px;
  background: rgba(0, 0, 0, 0.7);
  color: #fff;
}

.tooltip-box.visible {
  display: block;
}

.tooltip-arrow {
  position: absolute;
  top: -10px;
  left: 50%;
  border-width: 5px;
  border-style: solid;
  border-color: transparent transparent rgba(0, 0, 0, 0.7) transparent;
}
```

```jsx
const Tooltip = ({ children, text, ...rest }) => {
  const [show, setShow] = React.useState(false);

  return (
    <div className="tooltip-container">
      <div className={show ? "tooltip-box visible" : "tooltip-box"}>
        {text}
        <span className="tooltip-arrow" />
      </div>
      <div
        onMouseEnter={() => setShow(true)}
        onMouseLeave={() => setShow(false)}
        {...rest}
      >
        {children}
      </div>
    </div>
  );
};
```

ツールチップコンポーネントを使用するには、以下のコードで `ReactDOM.createRoot()` を呼び出します。

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Tooltip text="Simple tooltip">
    <button>Hover me!</button>
  </Tooltip>
);
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
