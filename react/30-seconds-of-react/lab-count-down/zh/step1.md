# 倒计时器

> VM 中已经提供了 `index.html` 和 `script.js`。一般来说，你只需要在 `script.js` 和 `style.css` 中添加代码。

这段代码创建了一个倒计时器，当时间归零的时候会打印一条消息。为了实现它，采取了以下步骤：

1. 使用 `useState()` 钩子创建一个状态变量 `time`，用于保存时间值。从属性中初始化它，并将其解构为各个组成部分。
2. 使用 `useState()` 钩子创建 `paused` 和 `over` 状态变量，用于在定时器暂停或时间用完时防止其计时。
3. 创建一个方法 `tick`，根据当前值更新时间值（即每秒减少一秒）。
4. 创建一个方法 `reset`，将所有状态变量重置为初始状态。
5. 使用 `useEffect()` 钩子通过 `setInterval()` 每秒调用一次 `tick` 方法，并在组件卸载时使用 `clearInterval()` 进行清理。
6. 使用 `String.prototype.padStart()` 将时间数组的每个部分填充为两个字符，以创建定时器的可视化表示。

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

请点击右下角的“Go Live”在 8080 端口运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
