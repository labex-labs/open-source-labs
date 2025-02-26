# 制御されていないテキストエリア要素

> VM 内には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

この関数は、親コンポーネントによって制御されていない `<textarea>` 要素をレンダリングします。入力値を親コンポーネントに渡すためにコールバック関数を使用します。

この関数を使用するには：

- 親コンポーネントから `defaultValue` プロップを渡して、入力フィールドの初期値とします。
- `onChange` イベントを使用して、`onValueChange` コールバックをトリガーし、新しい値を親に送信します。

```jsx
const TextArea = ({
  cols = 20,
  rows = 2,
  defaultValue,
  onValueChange,
  ...rest
}) => {
  return (
    <textarea
      cols={cols}
      rows={rows}
      defaultValue={defaultValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};
```

使用例：

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <TextArea
    placeholder="Insert some text here..."
    onValueChange={(val) => console.log(val)}
  />
);
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新して、ウェブページをプレビューできます。
