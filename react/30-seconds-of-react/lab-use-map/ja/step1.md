# React useMap フック

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加する必要があります。

- `useMap()` フックは、状態付きの `Map` オブジェクトと React フックを使用してそれを操作する一連の関数を作成します。
- `useState()` フックは、`initialValue` で `Map` 状態を初期化します。
- `useMemo()` フックは、状態セッターを使用して `map` 状態変数を操作する一連の不変のアクションを作成し、毎回新しい `Map` を作成します。
- `useMap()` フックは、`map` 状態変数と作成された `actions` を含む配列を返します。
- `MyApp` コンポーネントは、`useMap()` フックを使用して状態付きの `Map` オブジェクトを初期化し、`Map` から項目を追加、リセット、削除するためのボタンを提供します。
- `JSON.stringify()` 関数は、`Map` オブジェクトを読みやすい JSON 文字列にフォーマットします。

```jsx
const useMap = (initialValue) => {
  const [map, setMap] = React.useState(new Map(initialValue));

  const actions = React.useMemo(
    () => ({
      set: (key, value) =>
        setMap((prevMap) => {
          const nextMap = new Map(prevMap);
          nextMap.set(key, value);
          return nextMap;
        }),
      remove: (key) =>
        setMap((prevMap) => {
          const nextMap = new Map(prevMap);
          nextMap.delete(key);
          return nextMap;
        }),
      clear: () => setMap(new Map())
    }),
    [setMap]
  );

  return [map, actions];
};

const MyApp = () => {
  const [map, { set, remove, clear }] = useMap([["apples", 10]]);

  const handleAdd = () => set(Date.now(), new Date().toJSON());
  const handleReset = () => clear();
  const handleRemove = () => remove("apples");

  return (
    <div>
      <button onClick={handleAdd}>Add</button>
      <button onClick={handleReset}>Reset</button>
      <button onClick={handleRemove} disabled={!map.has("apples")}>
        Remove apples
      </button>
      <pre>{JSON.stringify(Object.fromEntries(map), null, 2)}</pre>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブ サービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
