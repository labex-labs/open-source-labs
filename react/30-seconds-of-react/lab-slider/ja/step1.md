# 制御されていない範囲入力

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

React でスライダーを作成するには、`Slider` コンポーネントを使用し、`min`、`max`、`defaultValue`、および `onValueChange` の各プロパティを渡します。

`Slider` コンポーネントでは、`<input>` 要素の `type` を `"range"` に設定してスライダーを作成します。親から渡された `defaultValue` プロパティを、制御されていない入力フィールドの初期値として使用します。`onChange` イベントを使用して、`onValueChange` コールバックをトリガーし、新しい値を親に送信します。

以下は、`Slider` コンポーネントのコードです。

```jsx
const Slider = ({
  min = 0,
  max = 100,
  defaultValue,
  onValueChange,
  ...rest
}) => {
  return (
    <input
      type="range"
      min={min}
      max={max}
      defaultValue={defaultValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};
```

`Slider` コンポーネントをレンダリングするには、`ReactDOM.createRoot` を使用して、`onValueChange` コールバック関数を渡します。

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Slider onValueChange={(val) => console.log(val)} />
);
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新して、ウェブページをプレビューできます。
