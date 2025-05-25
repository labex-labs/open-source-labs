# React useRequestAnimationFrame 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

각 리페인트 전에 애니메이션 함수를 실행하려면 `useRef()` 훅을 사용하여 `requestRef` 및 `previousTimeRef` 변수를 생성합니다. 그런 다음, 이러한 변수를 업데이트하고, `callback`을 실행하며, `Window.requestAnimationFrame()`을 영구적으로 호출하는 `animate()` 함수를 정의합니다. 마지막으로, 빈 배열과 함께 `useEffect()` 훅을 사용하여 `Window.requestAnimationFrame()`으로 `requestRef`의 값을 초기화하고, 컴포넌트가 언마운트될 때 반환된 값과 `Window.cancelAnimationFrame()`을 사용하여 정리합니다.

다음은 `useRequestAnimationFrame()`의 예시 구현입니다.

```jsx
const useRequestAnimationFrame = (callback) => {
  const requestRef = React.useRef();
  const previousTimeRef = React.useRef();

  const animate = (time) => {
    if (previousTimeRef.current) {
      callback(time - previousTimeRef.current);
    }
    previousTimeRef.current = time;
    requestRef.current = requestAnimationFrame(animate);
  };

  React.useEffect(() => {
    requestRef.current = requestAnimationFrame(animate);
    return () => cancelAnimationFrame(requestRef.current);
  }, []);
};
```

이 사용자 정의 훅을 컴포넌트에서 사용하려면 콜백 함수를 전달하기만 하면 됩니다. 예를 들어, 100 FPS 로 업데이트되는 간단한 카운터를 생성하려면 다음과 같이 합니다.

```jsx
const Counter = () => {
  const [count, setCount] = React.useState(0);

  useRequestAnimationFrame((deltaTime) => {
    setCount((prevCount) => (prevCount + deltaTime * 0.01) % 100);
  });

  return <p>{Math.round(count)}</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Counter />);
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음, **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
