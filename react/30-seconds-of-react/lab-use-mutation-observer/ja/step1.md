# React の useMutationObserver フック

> `index.html` と `script.js` はすでに仮想マシン (VM) に用意されています。一般的には、`script.js` と `style.css` にコードを追加するだけです。

DOM ツリーに加えられた変更を監視するには、`useMutationObserver` フックを使用できます。その仕組みは次の通りです。

1. このフックは 3 つのパラメーターを受け取ります。`ref`、`callback`、および `options` です。
2. フックの内部では、`callback` と `options` の値に依存する `useEffect()` フックが使用されます。
3. 与えられた `ref` が初期化されている場合、新しい `MutationObserver` が作成され、`callback` が渡されます。
4. `MutationObserver.observe()` が与えられた `options` で呼び出され、与えられた `ref` の変更を監視します。
5. コンポーネントがアンマウントされるときに、`MutationObserver.disconnect()` を使用して `ref` からオブザーバーを削除します。

コードは次のとおりです。

```jsx
const useMutationObserver = (
  ref,
  callback,
  options = {
    attributes: true,
    characterData: true,
    childList: true,
    subtree: true
  }
) => {
  React.useEffect(() => {
    if (!ref.current) return;

    const observer = new MutationObserver(callback);
    observer.observe(ref.current, options);

    return () => observer.disconnect();
  }, [callback, options, ref]);
};
```

`App` コンポーネントでは、`useMutationObserver` フックを使用して `mutationRef` 要素に加えられた変更を監視しています。`incrementMutationCount` 関数が `callback` として渡されています。

```jsx
const App = () => {
  const mutationRef = React.useRef();
  const [mutationCount, setMutationCount] = React.useState(0);

  const incrementMutationCount = React.useCallback(() => {
    setMutationCount((count) => count + 1);
  }, []);

  useMutationObserver(mutationRef, incrementMutationCount);

  const [content, setContent] = React.useState("Hello world");

  return (
    <>
      <label htmlFor="content-input">Edit this to update the text:</label>
      <textarea
        id="content-input"
        style={{ width: "100%" }}
        value={content}
        onChange={(e) => setContent(e.target.value)}
      />
      <div style={{ width: "100%" }} ref={mutationRef}>
        <div
          style={{
            resize: "both",
            overflow: "auto",
            maxWidth: "100%",
            border: "1px solid black"
          }}
        >
          <h2>Resize or change the content:</h2>
          <p>{content}</p>
        </div>
      </div>
      <div>
        <h3>Mutation count {mutationCount}</h3>
      </div>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

右下隅にある「Go Live」をクリックして、ポート 8080 で Web サービスを実行してください。その後、**Web 8080** タブを更新すると、Web ページをプレビューできます。
