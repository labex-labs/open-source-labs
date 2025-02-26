# React хук useOnGlobalEvent

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Эта функция выполняет обратную функцию каждый раз, когда событие возникает на глобальном объекте. Чтобы реализовать эту функцию:

1. Используйте хук `useRef()` для создания переменной `listener`, которая будет хранить ссылку на слушателя.
2. Используйте хук `useRef()` для создания переменной, которая будет хранить предыдущие значения аргументов `type` и `options`.
3. Используйте хук `useEffect()` и `EventTarget.addEventListener()` для прослушивания заданного события `type` на глобальном объекте `Window`.
4. Используйте `EventTarget.removeEventListener()` для удаления любых существующих слушателей и очистки при демонтировании компонента.

```jsx
const useOnGlobalEvent = (type, callback, options) => {
  const listener = React.useRef(null);
  const previousProps = React.useRef({ type, options });

  React.useEffect(() => {
    const { type: previousType, options: previousOptions } =
      previousProps.current;

    if (listener.current) {
      window.removeEventListener(
        previousType,
        listener.current,
        previousOptions
      );
    }

    listener.current = callback;
    window.addEventListener(type, callback, options);
    previousProps.current = { type, options };

    return () => {
      window.removeEventListener(type, listener.current, options);
    };
  }, [callback, type, options]);
};
```

Вот пример использования этой функции:

```jsx
const App = () => {
  useOnGlobalEvent("mousemove", (e) => {
    console.log(`(${e.x}, ${e.y})`);
  });

  return <p>Move your mouse around</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
