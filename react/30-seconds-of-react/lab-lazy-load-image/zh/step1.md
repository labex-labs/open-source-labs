# 图片懒加载

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

要渲染支持懒加载的图片，请按以下步骤操作：

1. 使用 `useState()` 钩子创建一个有状态的值，用于指示图片是否已加载。
2. 使用 `useEffect()` 钩子检查 `HTMLImageElement.prototype` 是否包含 `'loading'`。这将检查是否原生支持懒加载。如果不支持，则创建一个新的 `IntersectionObserver`，并使用 `IntersectionObserver.observer()` 来观察 `<img>` 元素。使用钩子的返回值在组件卸载时进行清理。
3. 使用 `useCallback()` 钩子来记忆 `IntersectionObserver` 的回调函数。此回调将更新 `isLoaded` 状态变量，并使用 `IntersectionObserver.disconnect()` 断开 `IntersectionObserver` 实例的连接。
4. 使用 `useRef()` 钩子创建两个引用。一个将保存 `<img>` 元素，另一个在必要时保存 `IntersectionObserver` 实例。
5. 最后，使用给定的属性渲染 `<img>` 元素。如有必要，应用 `loading='lazy'` 使其懒加载。使用 `isLoaded` 来确定 `src` 属性的值。

以下是这些步骤的示例实现：

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

要使用此 `LazyLoadImage` 组件，只需使用图片的 `src` 和 `alt` 属性调用它：

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <LazyLoadImage
    src="https://picsum.photos/id/1080/600/600"
    alt="Strawberries"
  />
);
```

请点击右下角的“Go Live”在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
