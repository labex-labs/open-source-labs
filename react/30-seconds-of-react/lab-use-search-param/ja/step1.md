# React useSearchParam フック

> VM 内には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

ブラウザのロケーション検索パラメータを追跡するには、次の手順を実行します。

1. `useCallback()` フックを使用してコールバックを作成します。コールバックでは、`URLSearchParams` コンストラクタを使用して、目的のパラメータの現在の値を取得します。

```jsx
const getValue = React.useCallback(
  () => new URLSearchParams(window.location.search).get(param),
  [param]
);
```

2. `useState()` フックを使用して、パラメータの現在の値を保持する状態変数を作成します。

```jsx
const [value, setValue] = React.useState(getValue);
```

3. `useEffect()` フックを使用して、マウント時に状態変数を更新するための適切なイベントリスナーを設定し、アンマウント時にそれらをクリーンアップします。

```jsx
React.useEffect(() => {
  const onChange = () => {
    setValue(getValue());
  };

  window.addEventListener("popstate", onChange);
  window.addEventListener("pushstate", onChange);
  window.addEventListener("replacestate", onChange);

  return () => {
    window.removeEventListener("popstate", onChange);
    window.removeEventListener("pushstate", onChange);
    window.removeEventListener("replacestate", onChange);
  };
}, []);
```

コンポーネントでこのカスタムフックを使用する方法の例を次に示します。

```jsx
const MyApp = () => {
  const post = useSearchParam("post");

  return (
    <>
      <p>Post param value: {post || "null"}</p>
      <button
        onClick={() =>
          history.pushState({}, "", location.pathname + "?post=42")
        }
      >
        View post 42
      </button>
      <button onClick={() => history.pushState({}, "", location.pathname)}>
        Exit
      </button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

この例では、`MyApp` コンポーネントが作成されており、これは `useSearchParam` カスタムフックを使用して、ロケーション検索内の `post` パラメータの値を追跡しています。`post` の値は段落タグに表示されます。また、ロケーション検索パラメータの値を変更する方法を示すために 2 つのボタンも用意されています。

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新して、ウェブページをプレビューできます。
