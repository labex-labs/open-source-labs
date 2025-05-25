# 카운트다운 타이머

> `index.html` 및 `script.js`는 이미 VM 에 제공되었습니다. 일반적으로 `script.js` 및 `style.css`에만 코드를 추가하면 됩니다.

이 코드는 0 에 도달하면 메시지를 출력하는 카운트다운 타이머를 생성합니다. 이를 구현하기 위해 다음 단계를 수행합니다.

1. `useState()` 훅을 사용하여 시간 값을 저장하는 `time` 상태 변수를 생성합니다. props 에서 초기화하고 구성 요소로 분해합니다.
2. `useState()` 훅을 사용하여 타이머가 일시 중지되었거나 시간이 다 된 경우 타이머가 틱하지 않도록 하는 `paused` 및 `over` 상태 변수를 생성합니다.
3. 현재 값을 기반으로 시간 값을 업데이트하는 `tick` 메서드를 생성합니다 (예: 시간을 1 초씩 감소).
4. 모든 상태 변수를 초기 상태로 재설정하는 `reset` 메서드를 생성합니다.
5. `useEffect()` 훅을 사용하여 `setInterval()`을 통해 매초 `tick` 메서드를 호출하고, 컴포넌트가 언마운트될 때 정리하기 위해 `clearInterval()`을 사용합니다.
6. `String.prototype.padStart()`를 사용하여 시간 배열의 각 부분을 두 문자로 채워 타이머의 시각적 표현을 만듭니다.

```jsx
const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
  const [paused, setPaused] = React.useState(false);
  const [over, setOver] = React.useState(false);
  const [[h, m, s], setTime] = React.useState([hours, minutes, seconds]);

  const tick = () => {
    if (paused || over) return;
    if (h === 0 && m === 0 && s === 0) setOver(true);
    else if (m === 0 && s === 0) setTime([h - 1, 59, 59]);
    else if (s == 0) setTime([h, m - 1, 59]);
    else setTime([h, m, s - 1]);
  };

  const reset = () => {
    setTime([parseInt(hours), parseInt(minutes), parseInt(seconds)]);
    setPaused(false);
    setOver(false);
  };

  React.useEffect(() => {
    const timerID = setInterval(tick, 1000);
    return () => clearInterval(timerID);
  });

  return (
    <div>
      <p>
        {`${h.toString().padStart(2, "0")}:${m.toString().padStart(2, "0")}:${s
          .toString()
          .padStart(2, "0")}`}
      </p>
      {over && <div>Time's up!</div>}
      <button onClick={() => setPaused(!paused)}>
        {paused ? "Resume" : "Pause"}
      </button>
      <button onClick={reset}>Restart</button>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <CountDown hours={1} minutes={45} />
);
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
