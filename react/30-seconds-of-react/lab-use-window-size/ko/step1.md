# React useWindowSize 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

브라우저 창의 크기를 추적하려면 다음 단계를 수행할 수 있습니다.

1. `useState()` 훅을 사용하여 창의 크기를 저장할 상태 변수 `windowSize`를 초기화합니다. 서버와 클라이언트 렌더링 간의 불일치를 방지하기 위해 두 값 모두 `undefined`로 초기화합니다.

```jsx
const [windowSize, setWindowSize] = React.useState({
  width: undefined,
  height: undefined
});
```

2. `Window.innerWidth` 및 `Window.innerHeight`를 사용하여 상태 변수를 업데이트하는 함수 `handleResize()`를 생성합니다. 이 함수는 `'resize'` 이벤트가 트리거될 때마다 호출됩니다.

```jsx
const handleResize = () =>
  setWindowSize({ width: window.innerWidth, height: window.innerHeight });
```

3. `useEffect()` 훅을 사용하여 마운트 시 `'resize'` 이벤트에 대한 적절한 리스너를 설정하고 언마운트 시 정리합니다.

```jsx
React.useEffect(() => {
  window.addEventListener("resize", handleResize);

  handleResize();

  return () => {
    window.removeEventListener("resize", handleResize);
  };
}, []);
```

모두 합쳐서 `useWindowSize()` 사용자 정의 훅은 다음과 같이 정의할 수 있습니다.

```jsx
const useWindowSize = () => {
  const [windowSize, setWindowSize] = React.useState({
    width: undefined,
    height: undefined
  });

  const handleResize = () =>
    setWindowSize({ width: window.innerWidth, height: window.innerHeight });

  React.useEffect(() => {
    window.addEventListener("resize", handleResize);

    handleResize();

    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []);

  return windowSize;
};
```

`useWindowSize()` 훅을 사용하려면 컴포넌트에서 호출하고 반환된 객체에서 `width` 및 `height` 값을 구조 분해 할당하면 됩니다.

```jsx
const MyApp = () => {
  const { width, height } = useWindowSize();

  return (
    <p>
      Window size: ({width} x {height})
    </p>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
