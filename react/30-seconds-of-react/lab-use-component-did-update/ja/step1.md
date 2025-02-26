# React の useComponentDidUpdate フック

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

このコードは、`useComponentDidUpdate` と呼ばれるカスタムフックを提供しており、コンポーネントが更新されるたびに指定された `callback` 関数を実行します。このフックがたどる手順は以下の通りです。

1. `useRef()` フックを使って `mounted` 変数を作成します。この変数はコンポーネントがマウントされたかどうかを追跡します。
2. `useEffect()` フックを使って、フックが最初に実行されたときに `mounted` の値を `true` に設定します。
3. その後のフックの実行時には、コンポーネントが既にマウントされている場合にのみ、指定された `callback` 関数を実行します。
4. 2番目の引数 `condition` が提供された場合、フックはその依存関係のいずれかが変更された場合にのみ実行されます。
5. このフックは、クラスコンポーネントの `componentDidUpdate()` ライフサイクルメソッドと同じように動作します。

以下がコードです。

```jsx
const useComponentDidUpdate = (callback, condition) => {
  const isMounted = React.useRef(false);
  React.useEffect(() => {
    if (isMounted.current) {
      callback();
    } else {
      isMounted.current = true;
    }
  }, condition);
};

const App = () => {
  const [value, setValue] = React.useState(0);
  const [otherValue, setOtherValue] = React.useState(1);

  useComponentDidUpdate(() => {
    console.log(`Current value is ${value}.`);
  }, [value]);

  return (
    <>
      <p>
        Value: {value}, other value: {otherValue}
      </p>
      <button onClick={() => setValue(value + 1)}>Increment value</button>
      <button onClick={() => setOtherValue(otherValue + 1)}>
        Increment other value
      </button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

右下隅の「Go Live」をクリックして、ポート8080でウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
