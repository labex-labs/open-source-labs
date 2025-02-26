# React useSetフック

> VM内には既に`index.html`と`script.js`が用意されています。一般的には、`script.js`と`style.css`にのみコードを追加すればよいです。

この関数は、状態付きの`Set`オブジェクトとその状態を操作できる関数のセットを作成します。

この関数を使用するには：

- `useState()`と`Set`コンストラクタを呼び出して、`initialValue`から新しい`Set`を作成します。
- `useMemo()`を使用して、`set`状態変数を操作できる非変更関数のセットを作成します。毎回状態セッターを使用して新しい`Set`を作成します。
- `set`状態変数と作成した`actions`の両方を返します。

この関数の例としての実装を以下に示します：

```jsx
const useSet = (initialValue) => {
  const [set, setSet] = React.useState(new Set(initialValue));

  const actions = React.useMemo(
    () => ({
      add: (item) => setSet((prevSet) => new Set([...prevSet, item])),
      remove: (item) =>
        setSet((prevSet) => new Set([...prevSet].filter((i) => i !== item))),
      clear: () => setSet(new Set())
    }),
    [setSet]
  );

  return [set, actions];
};
```

この関数の使用例を以下に示します：

```jsx
const MyApp = () => {
  const [set, { add, remove, clear }] = useSet(new Set(["apples"]));

  return (
    <div>
      <button onClick={() => add(String(Date.now()))}>Add</button>
      <button onClick={() => clear()}>Reset</button>
      <button onClick={() => remove("apples")} disabled={!set.has("apples")}>
        Remove apples
      </button>
      <pre>{JSON.stringify([...set], null, 2)}</pre>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

右下隅の「Go Live」をクリックして、ポート8080でウェブサービスを実行してください。その後、**Web 8080**タブを更新してウェブページをプレビューできます。
