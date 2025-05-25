# React useUnload 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

`beforeunload` 윈도우 이벤트는 다음 단계를 사용하여 처리할 수 있습니다.

1. `useRef()` 훅을 사용하여 콜백 함수 `fn`에 대한 ref 를 생성합니다.
2. 사용자가 창을 닫으려고 할 때 트리거되는 `'beforeunload'` 이벤트를 처리하기 위해 `useEffect()` 훅과 `EventTarget.addEventListener()`를 사용합니다.
3. 컴포넌트가 언마운트된 후 정리를 수행하기 위해 `EventTarget.removeEventListener()`를 사용합니다.

다음은 코드입니다.

```jsx
const useUnload = (fn) => {
  const callbackRef = React.useRef(fn);

  React.useEffect(() => {
    const callback = callbackRef.current;
    window.addEventListener("beforeunload", callback);
    return () => {
      window.removeEventListener("beforeunload", callback);
    };
  }, [callbackRef]);
};

const App = () => {
  useUnload((e) => {
    e.preventDefault();
    const exit = confirm("Are you sure you want to leave?");
    if (exit) window.close();
  });

  return <div>Try closing the window.</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
