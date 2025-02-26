# Хук useWindowSize в React

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Для отслеживания размеров окна браузера можно предпринять следующие шаги:

1. Используйте хук `useState()`, чтобы инициализировать переменную состояния `windowSize`, которая будет хранить размеры окна. Инициализируйте оба значения как `undefined`, чтобы избежать несоответствия между рендерами на сервере и клиенте.

```jsx
const [windowSize, setWindowSize] = React.useState({
  width: undefined,
  height: undefined
});
```

2. Создайте функцию `handleResize()`, которая использует `Window.innerWidth` и `Window.innerHeight` для обновления переменной состояния. Эта функция будет вызываться при каждом вызове события `'resize'`.

```jsx
const handleResize = () =>
  setWindowSize({ width: window.innerWidth, height: window.innerHeight });
```

3. Используйте хук `useEffect()`, чтобы установить соответствующий слушатель для события `'resize'` при монтировании и удалить его при демонтировании.

```jsx
React.useEffect(() => {
  window.addEventListener("resize", handleResize);

  handleResize();

  return () => {
    window.removeEventListener("resize", handleResize);
  };
}, []);
```

Вместе это выглядит так, и можно определить пользовательский хук `useWindowSize()` следующим образом:

```jsx
const useWindowSize = () => {
  const [windowSize, setWindowSize] = React.useState({
    width: undefined,
    height: undefined
  });

  const handleResize = () =>
    setWindowSize({ width: window.innerWidth, height: window.innerHeight });

  React.useEffect(() => {
    window.addEventListener("resize", handleResize);

    handleResize();

    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []);

  return windowSize;
};
```

Для использования хука `useWindowSize()` просто вызовите его в компоненте и деструктурируйте значения `width` и `height` из возвращаемого объекта.

```jsx
const MyApp = () => {
  const { width, height } = useWindowSize();

  return (
    <p>
      Размер окна: ({width} x {height})
    </p>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем можно обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
