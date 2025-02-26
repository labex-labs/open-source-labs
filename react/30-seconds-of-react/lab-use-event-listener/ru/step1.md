# React хук useEventListener

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Эта функция добавляет слушатель события для указанного типа события на заданном элементе. Чтобы использовать эту функцию, следуйте шагам:

1. Используйте хук `useRef()`, чтобы создать ref, который будет хранить `handler`.
2. Используйте хук `useEffect()`, чтобы обновить значение ref `savedHandler` каждый раз, когда меняется `handler`.
3. Используйте хук `useEffect()`, чтобы добавить слушатель события к заданному элементу и очистить его при демонтировании.
4. Пропустите последний аргумент, `el`, чтобы по умолчанию использовать `Window`.

Вот код:

```jsx
const useEventListener = (type, handler, el = window) => {
  const savedHandler = React.useRef(handler);

  React.useEffect(() => {
    savedHandler.current = handler;
  }, [handler]);

  React.useEffect(() => {
    const listener = (e) => savedHandler.current(e);

    el.addEventListener(type, listener);

    return () => {
      el.removeEventListener(type, listener);
    };
  }, [type, el]);
};
```

Вот пример использования функции `useEventListener()`:

```jsx
const MyApp = () => {
  const [coords, setCoords] = React.useState({ x: 0, y: 0 });

  const updateCoords = React.useCallback(
    ({ clientX, clientY }) => {
      setCoords({ x: clientX, y: clientY });
    },
    [setCoords]
  );

  useEventListener("mousemove", updateCoords);

  return (
    <p>
      Координаты мыши: {coords.x}, {coords.y}
    </p>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
