# 画像の遅延読み込み

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加する必要があります。

遅延読み込みをサポートする画像をレンダリングするには、次の手順に従います。

1. `useState()` フックを使用して、画像が読み込まれたかどうかを示す状態付き値を作成します。
2. `useEffect()` フックを使用して、`HTMLImageElement.prototype` に `'loading'` が含まれているかどうかを確認します。これは、ネイティブで遅延読み込みがサポートされているかどうかを確認します。サポートされていない場合は、新しい `IntersectionObserver` を作成し、`IntersectionObserver.observer()` を使用して `<img>` 要素を監視します。コンポーネントがアンマウントされたときにクリーンアップするために、フックの `return` 値を使用します。
3. `useCallback()` フックを使用して、`IntersectionObserver` 用のコールバック関数をメモ化します。このコールバックは、`isLoaded` 状態変数を更新し、`IntersectionObserver.disconnect()` を使用して `IntersectionObserver` インスタンスを切断します。
4. `useRef()` フックを使用して 2 つの ref を作成します。1 つは `<img>` 要素を保持し、もう 1 つは必要に応じて `IntersectionObserver` インスタンスを保持します。
5. 最後に、指定された属性で `<img>` 要素をレンダリングします。必要に応じて、`loading='lazy'` を適用して遅延読み込みを行います。`isLoaded` を使用して `src` 属性の値を決定します。

これらの手順の例としての実装は次のとおりです。

```jsx
const LazyLoadImage = ({
  alt,
  src,
  className,
  loadInitially = false,
  observerOptions = { root: null, rootMargin: "200px 0px" },
  ...props
}) => {
  const observerRef = React.useRef(null);
  const imgRef = React.useRef(null);
  const [isLoaded, setIsLoaded] = React.useState(loadInitially);

  const observerCallback = React.useCallback(
    (entries) => {
      if (entries[0].isIntersecting) {
        observerRef.current.disconnect();
        setIsLoaded(true);
      }
    },
    [observerRef]
  );

  React.useEffect(() => {
    if (loadInitially) return;

    if ("loading" in HTMLImageElement.prototype) {
      setIsLoaded(true);
      return;
    }

    observerRef.current = new IntersectionObserver(
      observerCallback,
      observerOptions
    );
    observerRef.current.observe(imgRef.current);
    return () => {
      observerRef.current.disconnect();
    };
  }, []);

  return (
    <img
      alt={alt}
      src={isLoaded ? src : ""}
      ref={imgRef}
      className={className}
      loading={loadInitially ? undefined : "lazy"}
      {...props}
    />
  );
};
```

この `LazyLoadImage` コンポーネントを使用するには、画像の `src` と `alt` 属性を指定して呼び出します。

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <LazyLoadImage
    src="https://picsum.photos/id/1080/600/600"
    alt="Strawberries"
  />
);
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
