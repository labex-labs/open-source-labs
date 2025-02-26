# トグル

> VM内には既に`index.html`と`script.js`が用意されています。一般的には、`script.js`と`style.css`にのみコードを追加すればよいです。

トグルコンポーネントをレンダリングするには、次の手順に従います。

1. `useState()`フックを使用して、`isToggledOn`状態変数を`defaultToggled`に初期化します。
2. `<input>`要素をレンダリングし、その`onClick`イベントをバインドして`isToggledOn`状態変数を更新します。ラッピングする`<label>`要素に適切な`className`を適用します。
3. 次のCSSを使用してトグルコンポーネントをスタイリッシュにします。

```css
.toggle input[type="checkbox"] {
  display: none;
}

.toggle.on {
  background-color: green;
}

.toggle.off {
  background-color: red;
}
```

以下がコードです。

```jsx
const Toggle = ({ defaultToggled = false }) => {
  const [isToggleOn, setIsToggleOn] = React.useState(defaultToggled);

  return (
    <label className={isToggleOn ? "toggle on" : "toggle off"}>
      <input
        type="checkbox"
        checked={isToggleOn}
        onChange={() => setIsToggleOn(!isToggleOn)}
      />
      {isToggleOn ? "ON" : "OFF"}
    </label>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Toggle />);
```

右下隅の「Go Live」をクリックして、ポート8080でウェブサービスを実行してください。その後、**Web 8080**タブを更新してウェブページをプレビューできます。
