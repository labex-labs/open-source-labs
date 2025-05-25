# React useOnWindowResize Hook

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

이 코드는 윈도우 크기가 변경될 때마다 콜백 함수를 실행합니다. 이를 구현하려면 다음 단계를 따르세요.

1. `useRef()` 훅을 사용하여 `listener`라는 변수를 생성합니다. 이 변수는 리스너에 대한 참조를 저장합니다.

2. `useEffect()` 훅과 `EventTarget.addEventListener()`를 사용하여 `Window` 전역 객체의 `'resize'` 이벤트를 수신합니다. 이벤트가 트리거되면 `callback` 함수를 호출합니다.

3. 컴포넌트가 언마운트될 때 `EventTarget.removeEventListener()`를 사용하여 기존 리스너를 제거하여 정리합니다.

다음은 코드입니다.

```jsx
const useOnWindowResize = (callback) => {
  const listener = React.useRef(null);

  React.useEffect(() => {
    if (listener.current) {
      window.removeEventListener("resize", listener.current);
    }
    listener.current = callback;
    window.addEventListener("resize", callback);
    return () => {
      window.removeEventListener("resize", callback);
    };
  }, [callback]);
};

const App = () => {
  useOnWindowResize(() =>
    console.log(`Window size: (${window.innerWidth}, ${window.innerHeight})`)
  );
  return <p>Resize the window and check the console.</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
