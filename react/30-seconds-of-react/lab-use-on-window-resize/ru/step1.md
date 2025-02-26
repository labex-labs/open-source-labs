# React-хук useOnWindowResize

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно добавить код только в `script.js` и `style.css`.

Этот код выполняет функцию обратного вызова каждый раз при изменении размеров окна. Чтобы реализовать это, вы должны следовать шагам:

1. Создайте переменную под названием `listener` с использованием хука `useRef()`. Эта переменная будет хранить ссылку на слушателя.

2. Используйте хук `useEffect()` и `EventTarget.addEventListener()` для прослушивания события `'resize'` глобального объекта `Window`. Когда событие срабатывает, вызовите функцию `callback`.

3. Очистите ресурсы, удалив любых существующих слушателей с помощью `EventTarget.removeEventListener()`, когда компонент размонтируется.

Вот код:

```jsx
const useOnWindowResize = (callback) => {
  const listener = React.useRef(null);

  React.useEffect(() => {
    if (listener.current) {
      window.removeEventListener("resize", listener.current);
    }
    listener.current = callback;
    window.addEventListener("resize", callback);
    return () => {
      window.removeEventListener("resize", callback);
    };
  }, [callback]);
};

const App = () => {
  useOnWindowResize(() =>
    console.log(`Размер окна: (${window.innerWidth}, ${window.innerHeight})`)
  );
  return <p>Измените размер окна и проверьте консоль.</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
