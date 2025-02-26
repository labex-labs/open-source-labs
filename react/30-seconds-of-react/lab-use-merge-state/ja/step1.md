# React の useMergeState フック

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

提供された新しい状態をマージすることで状態付きの値とそれを更新する関数を作成するには、`useState()` フックを使って状態変数を作成し、それを `initialState` に初期化します。既存の状態に提供された新しい状態をマージすることで状態変数を更新する関数を作成します。新しい状態が関数の場合、それに前の状態を引数として渡して呼び出し、結果を使います。引数が提供されない場合、状態変数は空のオブジェクト (`{}`) で初期化されます。次のコードは、`useMergeState` カスタムフックを使ってこれを実装する方法を示しています。

```jsx
const useMergeState = (initialState = {}) => {
  const [value, setValue] = React.useState(initialState);

  const mergeState = (newState) => {
    if (typeof newState === "function") {
      newState = newState(value);
    }
    setValue({ ...value, ...newState });
  };

  return [value, mergeState];
};
```

ここでは、`MyApp` というコンポーネントでの `useMergeState` フックの使用例を示します。

```jsx
const MyApp = () => {
  const [data, setData] = useMergeState({ name: "John", age: 20 });

  return (
    <>
      <input
        value={data.name}
        onChange={(e) => setData({ name: e.target.value })}
      />
      <button onClick={() => setData(({ age }) => ({ age: age - 1 }))}>
        -
      </button>
      {data.age}
      <button onClick={() => setData(({ age }) => ({ age: age + 1 }))}>
        +
      </button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
