# React useIsomporphicEffect フック

> VM 内には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

サーバー上での `useEffect()` とクライアント上での `useLayoutEffect()` を適切に使用するために、`typeof` を使って `Window` オブジェクトが定義されているかどうかを確認します。定義されている場合、`useLayoutEffect()` を返し、そうでなければ `useEffect()` を返します。これを実装する方法の例を以下に示します。

```jsx
const useIsomorphicEffect =
  typeof window !== "undefined" ? React.useLayoutEffect : React.useEffect;
```

その後、コード内では次の例のように `useIsomorphicEffect()` を使用できます。

```jsx
const MyApp = () => {
  useIsomorphicEffect(() => {
    window.console.log("Hello");
  }, []);

  return null;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

これにより、コンポーネントがマウントされたときにコンソールに 'Hello' が表示され、サーバーとクライアントの両方で正常に動作します。

右下隅の「Go Live」をクリックして 8080 番ポートでウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
