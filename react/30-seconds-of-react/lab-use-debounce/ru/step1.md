# React хук useDebounce

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Чтобы демпфировать заданное значение, вы можете создать пользовательский хук, который принимает `value` и `delay`. Используйте хук `useState()`, чтобы хранить демпфированное значение, и хук `useEffect()`, чтобы обновлять демпфированное значение каждый раз, когда `value` обновляется. Чтобы отложить вызов установщика предыдущей переменной состояния на `delay` миллисекунд, используйте `setTimeout()`. Чтобы очистить при демонтировании компонента, используйте `clearTimeout()`. Это особенно полезно при работе с вводом пользователя.

Вот пример реализации хука `useDebounce()`:

```jsx
const useDebounce = (value, delay) => {
  const [debouncedValue, setDebouncedValue] = React.useState(value);

  React.useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    return () => {
      clearTimeout(handler);
    };
  }, [value, delay]);

  return debouncedValue;
};
```

Вы можете использовать хук `useDebounce()` в компоненте так:

```jsx
const Counter = () => {
  const [value, setValue] = React.useState(0);
  const lastValue = useDebounce(value, 500);

  return (
    <div>
      <p>
        Текущее: {value} - Демпфированное: {lastValue}
      </p>
      <button onClick={() => setValue(value + 1)}>Увеличить</button>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Counter />);
```

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
