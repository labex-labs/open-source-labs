# 制御されていない入力フィールド

> VM には既に`index.html`と`script.js`が用意されています。一般的には、`script.js`と`style.css`にのみコードを追加すればよいです。

このコードは、コールバック関数を使って親に値の更新を通知する制御されていない`<input>`要素をレンダリングします。それを使うには：

- `defaultValue`プロップを使って親から初期値を渡します。
- 値の更新を処理するための`onValueChange`と呼ばれるコールバック関数を渡します。
- `onChange`イベントを使ってコールバックを実行し、新しい値を親に送信します。

以下は例です：

```jsx
const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
  return (
    <input
      defaultValue={defaultValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <UncontrolledInput
    type="text"
    placeholder="Insert some text here..."
    onValueChange={console.log}
  />
);
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080**タブを更新して、ウェブページをプレビューできます。
