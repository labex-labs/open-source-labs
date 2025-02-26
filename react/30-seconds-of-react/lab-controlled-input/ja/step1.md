# コントロールされた入力フィールド

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

このコード スニペットは、コールバック関数を利用して親に値の更新を通知するコントロールされた `<input>` 要素を提供します。その動作方法は以下の通りです。

- コントロールされた入力フィールドの値は、親から渡される `value` プロップによって決まります。
- ユーザーによって入力フィールドに行われた変更は、`onChange` イベントによってキャプチャされ、これが `onValueChange` コールバック関数をトリガーし、新しい値を親コンポーネントに戻します。
- 入力フィールドの値を更新するには、親はコントロールされた入力コンポーネントに渡す `value` プロップを更新する必要があります。

以下は、`ControlledInput` コンポーネントの例の実装であり、その後に `Form` コンポーネントでの使用例が示されています。

```jsx
const ControlledInput = ({ value, onValueChange, ...rest }) => {
  return (
    <input
      value={value}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};

const Form = () => {
  const [value, setValue] = React.useState("");

  return (
    <ControlledInput
      type="text"
      placeholder="Insert some text here..."
      value={value}
      onValueChange={setValue}
    />
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Form />);
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブ サービスを実行してください。その後、**Web 8080** タブを更新して、ウェブ ページをプレビューできます。
