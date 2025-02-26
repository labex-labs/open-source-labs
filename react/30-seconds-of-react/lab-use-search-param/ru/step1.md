# Хуки React useSearchParam

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Для отслеживания параметров поиска в адресе браузера используйте следующие шаги:

1. Создайте обратный вызов с использованием хука `useCallback()`. Обратный вызов должен использовать конструктор `URLSearchParams` для получения текущего значения нужного параметра.

```jsx
const getValue = React.useCallback(
  () => new URLSearchParams(window.location.search).get(param),
  [param]
);
```

2. Создайте переменную состояния, которая хранит текущее значение параметра, с использованием хука `useState()`.

```jsx
const [value, setValue] = React.useState(getValue);
```

3. Установите соответствующие слушатели событий для обновления переменной состояния при монтировании и очистите их при демонтировании с использованием хука `useEffect()`.

```jsx
React.useEffect(() => {
  const onChange = () => {
    setValue(getValue());
  };

  window.addEventListener("popstate", onChange);
  window.addEventListener("pushstate", onChange);
  window.addEventListener("replacestate", onChange);

  return () => {
    window.removeEventListener("popstate", onChange);
    window.removeEventListener("pushstate", onChange);
    window.removeEventListener("replacestate", onChange);
  };
}, []);
```

Вот пример того, как использовать этот пользовательский хук в компоненте:

```jsx
const MyApp = () => {
  const post = useSearchParam("post");

  return (
    <>
      <p>Значение параметра post: {post || "null"}</p>
      <button
        onClick={() =>
          history.pushState({}, "", location.pathname + "?post=42")
        }
      >
        Просмотреть пост 42
      </button>
      <button onClick={() => history.pushState({}, "", location.pathname)}>
        Выйти
      </button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

В этом примере создается компонент `MyApp`, который использует пользовательский хук `useSearchParam` для отслеживания значения параметра `post` в поиске по адресу. Значение `post` отображается в теге абзаца. Также включены две кнопки, чтобы показать, как изменить значение параметра поиска адреса.

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
