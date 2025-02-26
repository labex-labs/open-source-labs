# ReactのuseDebounceフック

> VM内には既に`index.html`と`script.js`が用意されています。一般的には、`script.js`と`style.css`にのみコードを追加すればよいです。

与えられた値をデバウンス処理するには、`value`と`delay`を受け取るカスタムフックを作成します。デバウンスされた値を格納するために`useState()`フックを使用し、`value`が更新されるたびにデバウンスされた値を更新するために`useEffect()`フックを使用します。前の状態変数のセッターの呼び出しを`delay`ミリ秒だけ遅らせるには、`setTimeout()`を使用します。コンポーネントがマウント解除される際にクリーンアップするには、`clearTimeout()`を使用します。これは、ユーザー入力を扱う際に特に役立ちます。

以下は、`useDebounce()`フックの例の実装です：

```jsx
const useDebounce = (value, delay) => {
  const [debouncedValue, setDebouncedValue] = React.useState(value);

  React.useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    return () => {
      clearTimeout(handler);
    };
  }, [value, delay]);

  return debouncedValue;
};
```

この`useDebounce()`フックをコンポーネントで使用する方法は以下の通りです：

```jsx
const Counter = () => {
  const [value, setValue] = React.useState(0);
  const lastValue = useDebounce(value, 500);

  return (
    <div>
      <p>
        Current: {value} - Debounced: {lastValue}
      </p>
      <button onClick={() => setValue(value + 1)}>Increment</button>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Counter />);
```

右下隅の「Go Live」をクリックして、ポート8080でウェブサービスを実行してください。その後、**Web 8080**タブを更新して、ウェブページをプレビューできます。
