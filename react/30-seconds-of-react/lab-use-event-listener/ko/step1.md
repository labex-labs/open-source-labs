# React useEventListener 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

이 함수는 지정된 이벤트 유형에 대한 이벤트 리스너를 주어진 요소에 추가합니다. 이 함수를 사용하려면 다음 단계를 따르세요.

1. `useRef()` 훅을 사용하여 `handler`를 저장할 ref 를 생성합니다.
2. `useEffect()` 훅을 사용하여 `handler`가 변경될 때마다 `savedHandler` ref 의 값을 업데이트합니다.
3. `useEffect()` 훅을 사용하여 주어진 요소에 이벤트 리스너를 추가하고 언마운트 시 정리합니다.
4. 마지막 인수 `el`을 생략하여 기본적으로 `Window`를 사용합니다.

다음은 코드입니다.

```jsx
const useEventListener = (type, handler, el = window) => {
  const savedHandler = React.useRef(handler);

  React.useEffect(() => {
    savedHandler.current = handler;
  }, [handler]);

  React.useEffect(() => {
    const listener = (e) => savedHandler.current(e);

    el.addEventListener(type, listener);

    return () => {
      el.removeEventListener(type, listener);
    };
  }, [type, el]);
};
```

다음은 `useEventListener()` 함수의 사용 예시입니다.

```jsx
const MyApp = () => {
  const [coords, setCoords] = React.useState({ x: 0, y: 0 });

  const updateCoords = React.useCallback(
    ({ clientX, clientY }) => {
      setCoords({ x: clientX, y: clientY });
    },
    [setCoords]
  );

  useEventListener("mousemove", updateCoords);

  return (
    <p>
      Mouse coordinates: {coords.x}, {coords.y}
    </p>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
