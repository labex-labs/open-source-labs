# Обратный отсчет времени

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Этот код создает обратный отсчет времени, который выводит сообщение, когда время достигнет нуля. Для его реализации предпринимаются следующие шаги:

1. Используйте хук `useState()`, чтобы создать переменную состояния `time`, которая хранит значение времени. Инициализируйте ее из свойств и деструктурируйте ее на компоненты.
2. Используйте хук `useState()`, чтобы создать переменные состояния `paused` и `over`, которые используются для предотвращения тика таймера, если он приостановлен или время истекло.
3. Создайте метод `tick`, который обновляет значения времени на основе текущего значения (то есть уменьшает время на одну секунду).
4. Создайте метод `reset`, который сбрасывает все переменные состояния в их исходные состояния.
5. Используйте хук `useEffect()`, чтобы вызывать метод `tick` каждую секунду с использованием `setInterval()` и использовать `clearInterval()` для очистки, когда компонент будет демонтирован.
6. Используйте `String.prototype.padStart()`, чтобы дополнить каждую часть массива времени до двух символов для создания визуального представления таймера.

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
      {over && <div>Время вышло!</div>}
      <button onClick={() => setPaused(!paused)}>
        {paused ? "Продолжить" : "Приостановить"}
      </button>
      <button onClick={reset}>Перезапустить</button>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <CountDown hours={1} minutes={45} />
);
```

Пожалуйста, нажмите кнопку "Запустить в браузере" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
