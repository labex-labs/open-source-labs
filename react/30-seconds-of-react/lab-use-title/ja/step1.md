# React useTitle フック

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

ページのタイトルを設定するには、`useTitle` というカスタムフックを使用できます。このフックは、`typeof` を使って `Document` が定義されているかどうかを確認します。定義されている場合、`useRef()` フックを使って `Document` の元のタイトルを格納します。その後、`useEffect()` フックを使ってコンポーネントがマウントされたときに `Document.title` を渡された値に設定し、アンマウントされたときにクリーンアップします。

```jsx
const useTitle = (title) => {
  const documentDefined = typeof document !== "undefined";
  const originalTitle = React.useRef(documentDefined ? document.title : null);

  React.useEffect(() => {
    if (!documentDefined) return;

    if (document.title !== title) {
      document.title = title;
    }

    return () => {
      document.title = originalTitle.current;
    };
  }, [title]);
};
```

サンプルコードでは、`Alert` コンポーネントが `useTitle` フックを使ってタイトルを "Alert" に設定しています。`MyApp` コンポーネントは、`Alert` コンポーネントを切り替えるボタンをレンダリングしています。

```jsx
const Alert = () => {
  useTitle("Alert");

  return (
    <div>
      <p>Alert! Title has changed</p>
    </div>
  );
};

const MyApp = () => {
  const [alertOpen, setAlertOpen] = React.useState(false);

  return (
    <div>
      <button onClick={() => setAlertOpen(!alertOpen)}>Toggle alert</button>
      {alertOpen && <Alert />}
    </div>
  );
};

ReactDOM.render(<MyApp />, document.getElementById("root"));
```

右下隅の「Go Live」をクリックして、ポート 8080 で Web サービスを実行してください。その後、**Web 8080** タブを更新して Web ページをプレビューできます。
