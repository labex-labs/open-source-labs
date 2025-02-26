# React useToggler フック

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

2 つの状態の間で切り替えられるブール型の状態変数を作成するには、次の手順に従います。

1. `useState()` フックを使って `value` 状態変数とそのセッターを作成します。
2. `value` 状態変数の値を切り替える関数を作成し、`useCallback()` フックを使ってメモ化します。
3. `value` 状態変数とメモ化された切り替え関数を返します。

以下は実装例です。

```jsx
const useToggler = (initialState) => {
  const [value, setValue] = React.useState(initialState);

  const toggleValue = React.useCallback(() => setValue((prev) => !prev), []);

  return [value, toggleValue];
};
```

その後、このフックをコンポーネントで次のように使うことができます。

```jsx
const Switch = () => {
  const [val, toggleVal] = useToggler(false);
  return <button onClick={toggleVal}>{val ? "ON" : "OFF"}</button>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Switch />);
```

右下隅の「Go Live」をクリックして 8080 番ポートでウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
