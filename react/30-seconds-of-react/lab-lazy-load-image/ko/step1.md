# 이미지 지연 로딩 (Lazy-Loading Image)

> `index.html` 및 `script.js`는 이미 VM 에 제공되어 있습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

지연 로딩을 지원하는 이미지를 렌더링하려면 다음 단계를 따르세요.

1. `useState()` 훅을 사용하여 이미지가 로드되었는지 여부를 나타내는 상태 값을 생성합니다.
2. `useEffect()` 훅을 사용하여 `HTMLImageElement.prototype`에 `'loading'`이 포함되어 있는지 확인합니다. 이는 지연 로딩이 기본적으로 지원되는지 확인합니다. 그렇지 않은 경우, 새로운 `IntersectionObserver`를 생성하고 `IntersectionObserver.observer()`를 사용하여 `<img>` 요소를 관찰합니다. 컴포넌트가 언마운트될 때 정리 (clean up) 하기 위해 훅의 `return` 값을 사용합니다.
3. `useCallback()` 훅을 사용하여 `IntersectionObserver`에 대한 콜백 함수를 메모이제이션합니다. 이 콜백은 `isLoaded` 상태 변수를 업데이트하고 `IntersectionObserver.disconnect()`를 사용하여 `IntersectionObserver` 인스턴스를 연결 해제합니다.
4. `useRef()` 훅을 사용하여 두 개의 ref 를 생성합니다. 하나는 `<img>` 요소를, 다른 하나는 필요한 경우 `IntersectionObserver` 인스턴스를 저장합니다.
5. 마지막으로, 주어진 속성으로 `<img>` 요소를 렌더링합니다. 필요한 경우 `loading='lazy'`를 적용하여 지연 로딩을 수행합니다. `isLoaded`를 사용하여 `src` 속성의 값을 결정합니다.

다음은 이러한 단계의 예시 구현입니다.

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

이 `LazyLoadImage` 컴포넌트를 사용하려면 이미지의 `src` 및 `alt` 속성으로 호출하기만 하면 됩니다.

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <LazyLoadImage
    src="https://picsum.photos/id/1080/600/600"
    alt="Strawberries"
  />
);
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
