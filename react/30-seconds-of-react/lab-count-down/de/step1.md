# Countdown Timer

> `index.html` und `script.js` wurden bereits in der VM bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Dieser Code erstellt einen Countdown-Timer, der eine Nachricht ausgibt, wenn er auf null erreicht. Um ihn zu implementieren, werden die folgenden Schritte durchgeführt:

1. Verwenden Sie den `useState()`-Hook, um eine Zustandsvariable `time` zu erstellen, die den Zeitwert enthält. Initialisieren Sie sie aus den Props und zerlegen Sie sie in ihre Komponenten.
2. Verwenden Sie den `useState()`-Hook, um die Zustandsvariablen `paused` und `over` zu erstellen, die verwendet werden, um zu verhindern, dass der Timer weiter zählt, wenn er pausiert ist oder die Zeit abgelaufen ist.
3. Erstellen Sie eine Methode `tick`, die die Zeitwerte basierend auf dem aktuellen Wert aktualisiert (d.h. die Zeit um eine Sekunde verringert).
4. Erstellen Sie eine Methode `reset`, die alle Zustandsvariablen auf ihre Anfangswerte zurücksetzt.
5. Verwenden Sie den `useEffect()`-Hook, um die `tick`-Methode alle Sekunde über `setInterval()` aufzurufen und `clearInterval()` verwenden, um aufzuräumen, wenn die Komponente abmontiert wird.
6. Verwenden Sie `String.prototype.padStart()`, um jedes Teil des Zeitarrays auf zwei Zeichen aufzurunden, um die visuelle Darstellung des Timers zu erstellen.

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

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
