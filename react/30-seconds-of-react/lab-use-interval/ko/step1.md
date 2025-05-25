# React useInterval 훅

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

선언적인 방식으로 `setInterval()`을 구현하려면 `callback`과 `delay`를 사용하는 커스텀 훅을 만들 수 있습니다. 첫 번째 단계는 `useRef()` 훅을 사용하여 콜백 함수에 대한 `ref`를 만드는 것입니다. 그런 다음 `useEffect()` 훅을 사용하여 콜백이 변경될 때마다 최신 `callback`을 기억합니다. 마지막으로 `delay`에 종속된 `useEffect()` 훅을 사용하여 간격을 설정하고 정리합니다.

다음은 커스텀 훅에 대한 코드 스니펫 예시입니다.

```jsx
const useInterval = (callback, delay) => {
  const savedCallback = React.useRef();

  React.useEffect(() => {
    savedCallback.current = callback;
  }, [callback]);

  React.useEffect(() => {
    const tick = () => {
      savedCallback.current();
    };
    if (delay !== null) {
      let id = setInterval(tick, delay);
      return () => clearInterval(id);
    }
  }, [delay]);
};
```

그런 다음 이 커스텀 훅을 컴포넌트에서 사용할 수 있습니다. 예를 들어, 매 초마다 업데이트되는 타이머를 만들려면 다음과 같이 할 수 있습니다.

```jsx
const Timer = (props) => {
  const [seconds, setSeconds] = React.useState(0);

  useInterval(() => {
    setSeconds(seconds + 1);
  }, 1000);

  return <p>{seconds}</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Timer />);
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
