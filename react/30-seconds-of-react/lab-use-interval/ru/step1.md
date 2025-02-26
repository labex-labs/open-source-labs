# React хук useInterval

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Для реализации `setInterval()` декларативным способом вы можете создать пользовательский хук, который принимает `callback` и `delay`. Первым шагом является использование хука `useRef()` для создания `ref` для функции обратного вызова. Затем используйте хук `useEffect()` для запоминания последнего `callback` при любом его изменении. Наконец, используйте хук `useEffect()`, зависящий от `delay`, для настройки интервала и очистки.

Вот примерный фрагмент кода для пользовательского хука:

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

Затем вы можете использовать этот пользовательский хук в своих компонентах. Например, чтобы создать таймер, обновляющийся каждую секунду:

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

Пожалуйста, нажмите кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
