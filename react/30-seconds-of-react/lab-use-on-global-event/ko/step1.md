# React useOnGlobalEvent 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

이 함수는 전역 객체에서 이벤트가 발생할 때마다 콜백 함수를 실행합니다. 이 함수를 구현하려면 다음을 수행하십시오.

1. `useRef()` 훅을 사용하여 리스너 참조를 저장할 변수 `listener`를 생성합니다.
2. `useRef()` 훅을 사용하여 `type` 및 `options` 인수의 이전 값을 저장할 변수를 생성합니다.
3. `useEffect()` 훅과 `EventTarget.addEventListener()`를 사용하여 `Window` 전역 객체에서 주어진 이벤트 `type`을 수신 대기합니다.
4. 컴포넌트가 언마운트될 때 기존 리스너를 제거하고 정리하려면 `EventTarget.removeEventListener()`를 사용합니다.

```jsx
const useOnGlobalEvent = (type, callback, options) => {
  const listener = React.useRef(null);
  const previousProps = React.useRef({ type, options });

  React.useEffect(() => {
    const { type: previousType, options: previousOptions } =
      previousProps.current;

    if (listener.current) {
      window.removeEventListener(
        previousType,
        listener.current,
        previousOptions
      );
    }

    listener.current = callback;
    window.addEventListener(type, callback, options);
    previousProps.current = { type, options };

    return () => {
      window.removeEventListener(type, listener.current, options);
    };
  }, [callback, type, options]);
};
```

이 함수를 사용하는 방법의 예는 다음과 같습니다.

```jsx
const App = () => {
  useOnGlobalEvent("mousemove", (e) => {
    console.log(`(${e.x}, ${e.y})`);
  });

  return <p>Move your mouse around</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
