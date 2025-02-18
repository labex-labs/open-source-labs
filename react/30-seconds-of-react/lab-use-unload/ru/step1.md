# Хук React useUnload

> Файлы `index.html` и `script.js` уже предоставлены в виртуальной машине (VM). В общем, вам нужно только добавить код в `script.js` и `style.css`.

Событие окна `beforeunload` можно обработать с помощью следующих шагов:

1. Создайте ссылку (ref) для функции обратного вызова (callback function) `fn` с использованием хука `useRef()`.
2. Используйте хук `useEffect()` и метод `EventTarget.addEventListener()` для обработки события `'beforeunload'`, которое срабатывает, когда пользователь собирается закрыть окно.
3. Используйте метод `EventTarget.removeEventListener()` для выполнения очистки после того, как компонент будет демонтирован.

Вот код:

```jsx
const useUnload = (fn) => {
  const callbackRef = React.useRef(fn);

  React.useEffect(() => {
    const callback = callbackRef.current;
    window.addEventListener("beforeunload", callback);
    return () => {
      window.removeEventListener("beforeunload", callback);
    };
  }, [callbackRef]);
};

const App = () => {
  useUnload((e) => {
    e.preventDefault();
    const exit = confirm("Are you sure you want to leave?");
    if (exit) window.close();
  });

  return <div>Try closing the window.</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Нажмите на кнопку 'Go Live' в правом нижнем углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы предварительно просмотреть веб-страницу.
