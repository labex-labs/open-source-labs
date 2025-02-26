# React хук usePrevious

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Чтобы сохранить предыдущее состояние или свойства, вы можете создать пользовательский хук. Вот шаги:

1. Определите пользовательский хук, который принимает аргумент `value`.
2. Используйте хук `useRef()` для создания `ref` для `value`.
3. Используйте хук `useEffect()` для запоминания последнего значения `value`.
4. Верните значение `ref.current`.

```jsx
const usePrevious = (value) => {
  const ref = React.useRef();
  React.useEffect(() => {
    ref.current = value;
  });
  return ref.current;
};
```

Вот пример использования хука `usePrevious`:

```jsx
const Counter = () => {
  const [value, setValue] = React.useState(0);
  const lastValue = usePrevious(value);

  return (
    <div>
      <p>
        Текущее: {value} - Предыдущее: {lastValue}
      </p>
      <button onClick={() => setValue(value + 1)}>Увеличить</button>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Counter />);
```

Компонент `Counter` отображает текущее и предыдущее значения `value`. Когда нажимается кнопка `Увеличить`, значение `value` обновляется, а предыдущее значение сохраняется с использованием хука `usePrevious`.

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
