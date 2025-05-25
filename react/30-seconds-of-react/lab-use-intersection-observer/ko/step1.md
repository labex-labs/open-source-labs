# React useIntersectionObserver 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

주어진 요소의 가시성 변화를 관찰하려면 다음 단계를 따르세요.

1. `useState()` 훅을 사용하여 주어진 요소의 교차 값을 저장합니다.
2. 주어진 `options`와 `isIntersecting` 상태 변수를 업데이트하는 적절한 콜백을 사용하여 `IntersectionObserver`를 생성합니다.
3. 컴포넌트를 마운트할 때 `useEffect()` 훅을 사용하여 `IntersectionObserver.observe()`를 호출하고, 언마운트할 때 `IntersectionObserver.unobserve()`를 사용하여 정리합니다.

다음은 구현 예시입니다.

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

`useIntersectionObserver` 훅은 다음과 같이 사용할 수 있습니다.

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

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하세요. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
