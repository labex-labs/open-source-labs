# カウントダウンタイマー

> VM 内には既に`index.html`と`script.js`が用意されています。一般的には、`script.js`と`style.css`にのみコードを追加すればよいです。

このコードは、ゼロに達したときにメッセージを表示するカウントダウンタイマーを作成します。それを実装するには、以下の手順を踏みます。

1. `useState()`フックを使って、時間値を保持する状態変数`time`を作成します。props から初期化し、それをコンポーネントに分解します。
2. `useState()`フックを使って、タイマーが一時停止している場合や時間が切れている場合にタイマーがカウントダウンしないようにするための`paused`と`over`の状態変数を作成します。
3. 現在の値に基づいて時間値を更新する（つまり、1 秒ごとに時間を減らす）`tick`メソッドを作成します。
4. すべての状態変数を初期状態にリセットする`reset`メソッドを作成します。
5. `useEffect()`フックを使って、`setInterval()`を使って毎秒`tick`メソッドを呼び出し、コンポーネントがアンマウントされたときにクリーンアップするために`clearInterval()`を使います。
6. `String.prototype.padStart()`を使って、時間配列の各部分を 2 桁に埋めてタイマーの視覚的表現を作成します。

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

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080**タブを更新してウェブページをプレビューできます。
