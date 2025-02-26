# React хук useRequestAnimationFrame

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Для запуска функции анимации перед каждым перерисованием используйте хук `useRef()`, чтобы создать переменные `requestRef` и `previousTimeRef`. Затем определите функцию `animate()`, которая обновляет эти переменные, запускает `callback` и постоянно вызывает `Window.requestAnimationFrame()`. Наконец, используйте хук `useEffect()` с пустым массивом, чтобы инициализировать значение `requestRef` с помощью `Window.requestAnimationFrame()`, и используйте возвращаемое значение и `Window.cancelAnimationFrame()`, чтобы очистить ресурсы при размонтировании компонента.

Вот пример реализации `useRequestAnimationFrame()`:

```jsx
const useRequestAnimationFrame = (callback) => {
  const requestRef = React.useRef();
  const previousTimeRef = React.useRef();

  const animate = (time) => {
    if (previousTimeRef.current) {
      callback(time - previousTimeRef.current);
    }
    previousTimeRef.current = time;
    requestRef.current = requestAnimationFrame(animate);
  };

  React.useEffect(() => {
    requestRef.current = requestAnimationFrame(animate);
    return () => cancelAnimationFrame(requestRef.current);
  }, []);
};
```

Для использования этого пользовательского хука в компоненте просто передайте ему функцию обратного вызова. Например, чтобы создать простой счетчик, который обновляется с частотой 100 кадров в секунду:

```jsx
const Counter = () => {
  const [count, setCount] = React.useState(0);

  useRequestAnimationFrame((deltaTime) => {
    setCount((prevCount) => (prevCount + deltaTime * 0.01) % 100);
  });

  return <p>{Math.round(count)}</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Counter />);
```

Пожалуйста, нажмите кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
