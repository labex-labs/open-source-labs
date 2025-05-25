# React useTimeout 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

`setTimeout()`을 선언적으로 구현하려면 `callback`과 `delay`를 인수로 받는 커스텀 훅을 만듭니다. `useRef()` 훅을 사용하여 콜백 함수에 대한 `ref`를 생성하고, `useEffect()` 훅을 사용하여 최신 콜백을 기억합니다. 그런 다음 `useEffect()` 훅을 사용하여 타임아웃을 설정하고 정리합니다.

다음은 이 접근 방식을 보여주는 코드 스니펫입니다.

```jsx
const useTimeout = (callback, delay) => {
  const savedCallback = React.useRef();

  React.useEffect(() => {
    savedCallback.current = callback;
  }, [callback]);

  React.useEffect(() => {
    const tick = () => {
      savedCallback.current();
    };
    if (delay !== null) {
      let id = setTimeout(tick, delay);
      return () => clearTimeout(id);
    }
  }, [delay]);
};

const OneSecondTimer = (props) => {
  const [seconds, setSeconds] = React.useState(0);

  useTimeout(() => {
    setSeconds(seconds + 1);
  }, 1000);

  return <p>{seconds}</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<OneSecondTimer />);
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
