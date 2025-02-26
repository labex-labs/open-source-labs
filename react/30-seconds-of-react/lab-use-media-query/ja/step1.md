# React useMediaQuery フック

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

この関数は、現在の環境が指定されたメディアクエリに一致するかどうかを確認し、適切な値を返します。

- まず、`Window` と `Window.matchMedia()` が存在するかどうかを確認します。存在しない場合（例えば SSR 環境やサポートされていないブラウザの場合）、`whenFalse` を返します。
- `Window.matchMedia()` を使って指定された `query` と一致させます。その `matches` プロパティをブール値にキャストし、`useState()` フックを使って状態変数 `match` に格納します。
- `useEffect()` フックを使って変更のリスナーを追加し、フックが破棄された後にリスナーをクリーンアップします。
- 最後に、`match` の値に基づいて `whenTrue` または `whenFalse` を返します。

```jsx
const useMediaQuery = (query, whenTrue, whenFalse) => {
  if (
    typeof window === "undefined" ||
    typeof window.matchMedia === "undefined"
  ) {
    return whenFalse;
  }

  const mediaQuery = window.matchMedia(query);
  const [match, setMatch] = React.useState(!!mediaQuery.matches);

  React.useEffect(() => {
    const handler = () => setMatch(!!mediaQuery.matches);
    mediaQuery.addListener(handler);
    return () => mediaQuery.removeListener(handler);
  }, [mediaQuery]);

  return match ? whenTrue : whenFalse;
};
```

```jsx
const ResponsiveText = () => {
  const text = useMediaQuery(
    "(max-width: 400px)",
    "Less than 400px wide",
    "More than 400px wide"
  );

  return <span>{text}</span>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<ResponsiveText />);
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
