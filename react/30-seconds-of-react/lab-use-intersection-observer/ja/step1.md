# React useIntersectionObserver フック

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

特定の要素の表示状態の変化を監視するには、次の手順に従います。

1. `useState()` フックを使用して、特定の要素の交差値を格納します。
2. 与えられた `オプション` と適切なコールバックを持つ `IntersectionObserver` を作成して、`isIntersecting` 状態変数を更新します。
3. `useEffect()` フックを使用して、コンポーネントのマウント時に `IntersectionObserver.observe()` を呼び出し、アンマウント時に `IntersectionObserver.unobserve()` を使用してクリーンアップします。

以下は、実装例です。

```jsx
const useIntersectionObserver = (ref, options) => {
  const [isIntersecting, setIsIntersecting] = React.useState(false);

  React.useEffect(() => {
    const observer = new IntersectionObserver(([entry]) => {
      setIsIntersecting(entry.isIntersecting);
    }, options);

    if (ref.current) {
      observer.observe(ref.current);
    }

    return () => {
      observer.unobserve(ref.current);
    };
  }, [ref, options]);

  return isIntersecting;
};
```

`useIntersectionObserver` フックを次のように使用できます。

```jsx
const MyApp = () => {
  const ref = React.useRef();
  const onScreen = useIntersectionObserver(ref, { threshold: 0.5 });

  return (
    <div>
      <div style={{ height: "100vh" }}>Scroll down</div>
      <div style={{ height: "100vh" }} ref={ref}>
        <p>{onScreen ? "Element is on screen." : "Scroll more!"}</p>
      </div>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブ サービスを実行してください。その後、**Web 8080** タブを更新して、ウェブ ページをプレビューできます。
