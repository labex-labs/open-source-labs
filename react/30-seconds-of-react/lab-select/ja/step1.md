# 制御されていない`<select>`要素

> VM 内には既に`index.html`と`script.js`が用意されています。一般的には、`script.js`と`style.css`にのみコードを追加すればよいです。

これは、制御された`<select>`要素をレンダリングするコンポーネントです。このコンポーネントは、値の配列とコールバック関数を受け取り、選択された値を親コンポーネントに渡します。このコンポーネントを使用する手順は以下の通りです。

- `selectedValue`プロップを使用して`<select>`要素の初期値を設定します。
- `onValueChange`プロップを使用して、`<select>`要素の値が変更されたときに呼び出されるコールバック関数を指定します。
- `values`配列に対して`Array.prototype.map()`を使用して、渡された各値に対して`<option>`要素を作成します。
- `values`の各項目は 2 要素の配列である必要があり、最初の要素は項目の`value`で、2 番目の要素はその表示テキストです。

```jsx
const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
  return (
    <select
      defaultValue={selectedValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    >
      {values.map(([value, text]) => (
        <option key={value} value={value}>
          {text}
        </option>
      ))}
    </select>
  );
};
```

このコンポーネントを使用する方法の例は以下の通りです。

```jsx
const choices = [
  ["grapefruit", "Grapefruit"],
  ["lime", "Lime"],
  ["coconut", "Coconut"],
  ["mango", "Mango"]
];

ReactDOM.createRoot(document.getElementById("root")).render(
  <Select
    values={choices}
    selectedValue="lime"
    onValueChange={(val) => console.log(val)}
  />
);
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080**タブを更新してウェブページをプレビューできます。
