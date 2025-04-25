# React の useHash フック

> VM 内には既に`index.html`と`script.js`が用意されています。一般的には、`script.js`と`style.css`にのみコードを追加すればよいです。

このコードは、ブラウザのロケーションハッシュ値を追跡して更新します。それを使用するには、次の手順に従ってください。

1. `useState()`フックを使用して、`Location`オブジェクトの`hash`プロパティを遅延取得します。
2. `useCallback()`フックを使用して、`'hashchange'`イベントが発生したときに`hash`状態を更新するハンドラを作成します。
3. `useEffect()`フックを使用して、マウント時に`'hashchange'`イベントのリスナーを追加し、アンマウント時にそれをクリーンアップします。
4. `useCallback()`フックを使用して、与えられた値で`Location`オブジェクトの`hash`プロパティを更新する関数を作成します。
5. コンポーネント内で、`useHash()`を呼び出して現在の`hash`値を取得し、それを変更するための`updateHash()`関数を取得します。
6. `updateHash()`関数を使用して`hash`値を変更します。
7. コンポーネント内で現在の`hash`値をレンダリングします。
8. ユーザーが`hash`値を変更できる入力フィールドを作成します。

以下がコードです。

```jsx
const useHash = () => {
  const [hash, setHash] = React.useState(() => window.location.hash);

  const hashChangeHandler = React.useCallback(() => {
    setHash(window.location.hash);
  }, []);

  React.useEffect(() => {
    window.addEventListener("hashchange", hashChangeHandler);
    return () => {
      window.removeEventListener("hashchange", hashChangeHandler);
    };
  }, []);

  const updateHash = React.useCallback(
    (newHash) => {
      if (newHash !== hash) window.location.hash = newHash;
    },
    [hash]
  );

  return [hash, updateHash];
};

const MyApp = () => {
  const [hash, setHash] = useHash();

  React.useEffect(() => {
    setHash("#list");
  }, []);

  return (
    <>
      <p>Current hash value: {hash}</p>
      <p>Edit hash: </p>
      <input value={hash} onChange={(e) => setHash(e.target.value)} />
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

右下隅の「Go Live」をクリックして、ポート 8080 で Web サービスを実行してください。その後、**Web 8080**タブを更新して Web ページをプレビューできます。
