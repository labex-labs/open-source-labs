# React useMediaQuery 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

이 함수는 현재 환경이 주어진 미디어 쿼리와 일치하는지 확인하고 적절한 값을 반환합니다.

- 먼저, `Window` 및 `Window.matchMedia()`가 존재하는지 확인합니다. 존재하지 않는 경우 (예: SSR 환경 또는 지원되지 않는 브라우저) `whenFalse`를 반환합니다.
- `Window.matchMedia()`를 사용하여 주어진 `query`를 일치시킵니다. 해당 `matches` 속성을 부울 값으로 캐스팅하고 `useState()` 훅을 사용하여 `match`라는 상태 변수에 저장합니다.
- `useEffect()` 훅을 사용하여 변경 사항에 대한 리스너를 추가하고 훅이 파괴된 후 리스너를 정리합니다.
- 마지막으로, `match`의 값에 따라 `whenTrue` 또는 `whenFalse`를 반환합니다.

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

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
