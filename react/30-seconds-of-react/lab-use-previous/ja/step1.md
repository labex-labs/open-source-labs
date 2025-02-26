# React usePrevious フック

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

前の状態や props を保存するには、カスタムフックを作成できます。以下が手順です。

1. `value` 引数を持つカスタムフックを定義します。
2. `useRef()` フックを使用して、`value` 用の `ref` を作成します。
3. `useEffect()` フックを使用して、最新の `value` を覚えておきます。
4. `ref.current` の値を返します。

```jsx
const usePrevious = (value) => {
  const ref = React.useRef();
  React.useEffect(() => {
    ref.current = value;
  });
  return ref.current;
};
```

`usePrevious` フックを使用する例を以下に示します。

```jsx
const Counter = () => {
  const [value, setValue] = React.useState(0);
  const lastValue = usePrevious(value);

  return (
    <div>
      <p>
        Current: {value} - Previous: {lastValue}
      </p>
      <button onClick={() => setValue(value + 1)}>Increment</button>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Counter />);
```

`Counter` コンポーネントは、`value` の現在値と前の値を表示します。`Increment` ボタンがクリックされると、`value` が更新され、前の値は `usePrevious` フックを使用して保存されます。

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新して、ウェブページをプレビューできます。
