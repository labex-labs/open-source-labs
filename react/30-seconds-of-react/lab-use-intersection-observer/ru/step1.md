# Хук React useIntersectionObserver

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Для наблюдения за изменениями видимости заданного элемента следуйте шагам:

1. Используйте хук `useState()`, чтобы хранить значение пересечения заданного элемента.
2. Создайте `IntersectionObserver` с заданными `options` и соответствующим коллбэком для обновления переменной состояния `isIntersecting`.
3. Используйте хук `useEffect()`, чтобы вызвать `IntersectionObserver.observe()` при монтировании компонента и очистить с использованием `IntersectionObserver.unobserve()` при демонтировании.

Вот пример реализации:

```jsx
const useIntersectionObserver = (ref, options) => {
  const [isIntersecting, setIsIntersecting] = React.useState(false);

  React.useEffect(() => {
    const observer = new IntersectionObserver(([entry]) => {
      setIsIntersecting(entry.isIntersecting);
    }, options);

    if (ref.current) {
      observer.observe(ref.current);
    }

    return () => {
      observer.unobserve(ref.current);
    };
  }, [ref, options]);

  return isIntersecting;
};
```

Вы можете использовать хук `useIntersectionObserver` так:

```jsx
const MyApp = () => {
  const ref = React.useRef();
  const onScreen = useIntersectionObserver(ref, { threshold: 0.5 });

  return (
    <div>
      <div style={{ height: "100vh" }}>Scroll down</div>
      <div style={{ height: "100vh" }} ref={ref}>
        <p>{onScreen ? "Element is on screen." : "Scroll more!"}</p>
      </div>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Пожалуйста, нажмите на кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
