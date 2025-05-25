# React useSSR 훅

> `index.html`과 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js`와 `style.css`에만 코드를 추가하면 됩니다.

코드가 브라우저에서 실행되는지 서버에서 실행되는지 확인하려면, `typeof`, `Window`, `Window.document`, 그리고 `Document.createElement()`를 사용하여 DOM 의 가용성을 판단하는 사용자 정의 훅을 만듭니다. `useState()` 훅을 사용하여 `inBrowser` 상태 변수를 정의하고, `useEffect()` 훅을 사용하여 이를 업데이트하고 종료 시 정리합니다. `useMemo()` 훅을 사용하여 사용자 정의 훅의 반환 값을 메모이제이션 (memoization) 합니다.

다음은 코드입니다:

```jsx
const isDOMavailable = !!(
  typeof window !== "undefined" &&
  window.document &&
  window.document.createElement
);

const useSSR = () => {
  const [inBrowser, setInBrowser] = React.useState(isDOMavailable);

  React.useEffect(() => {
    setInBrowser(isDOMavailable);
    return () => {
      setInBrowser(false);
    };
  }, []);

  const useSSRObject = React.useMemo(
    () => ({
      isBrowser: inBrowser,
      isServer: !inBrowser,
      canUseWorkers: typeof Worker !== "undefined",
      canUseEventListeners: inBrowser && !!window.addEventListener,
      canUseViewport: inBrowser && !!window.screen
    }),
    [inBrowser]
  );

  return useSSRObject;
};

const SSRChecker = (props) => {
  const { isBrowser, isServer } = useSSR();

  return <p>{isBrowser ? "Running on browser" : "Running on server"}</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<SSRChecker />);
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음, **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
