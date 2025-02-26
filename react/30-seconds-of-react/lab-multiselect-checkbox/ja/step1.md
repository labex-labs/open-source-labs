# 複数選択可能な状態保持チェックボックス

> VM内には既に`index.html`と`script.js`が用意されています。一般的には、`script.js`と`style.css`にのみコードを追加すればよいです。

このコードは、チェックボックスのリストをレンダリングし、コールバック関数を使って選択された値を親コンポーネントに送信します。作成手順は以下の通りです。

1. `useState()`フックを使って、`options`プロップで`data`状態変数を初期化します。
2. 選択されたオプションで`data`状態変数を更新し、それらを使って`onChange`コールバック関数を呼び出す`toggle`関数を作成します。
3. 個々のチェックボックスとそのラベルを生成するために`data`状態変数をマッピングします。各チェックボックスの`onClick`ハンドラに`toggle`関数をバインドします。

```jsx
const MultiselectCheckbox = ({ options, onChange }) => {
  const [data, setData] = React.useState(options);

  const toggle = (index) => {
    const newData = [...data];
    newData[index] = {
      ...newData[index],
      checked: !newData[index].checked
    };
    setData(newData);
    onChange(newData.filter((item) => item.checked));
  };

  return (
    <>
      {data.map((item, index) => (
        <label key={item.label}>
          <input
            type="checkbox"
            checked={item.checked || false}
            onChange={() => toggle(index)}
          />
          {item.label}
        </label>
      ))}
    </>
  );
};
```

使用例は以下の通りです。

```jsx
const options = [{ label: "Item One" }, { label: "Item Two" }];

ReactDOM.createRoot(document.getElementById("root")).render(
  <MultiselectCheckbox
    options={options}
    onChange={(selected) => {
      console.log(selected);
    }}
  />
);
```

右下隅の「Go Live」をクリックして、ポート8080でウェブサービスを実行してください。その後、**Web 8080**タブを更新してウェブページをプレビューできます。
