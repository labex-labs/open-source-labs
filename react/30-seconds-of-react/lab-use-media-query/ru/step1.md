# Хук useMediaQuery в React

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Эта функция проверяет, соответствует ли текущая среда заданному медиа-запросу, и возвращает соответствующее значение.

- Во - первых, проверьте, существует ли `Window` и `Window.matchMedia()`. Если нет (например, в SSR - окружении или не поддерживаемом браузере), верните `whenFalse`.
- Используйте `Window.matchMedia()` для сопоставления заданного `query`. Преобразуйте его свойство `matches` в булево значение и сохраните его в переменной состояния, `match`, с использованием хука `useState()`.
- Используйте хук `useEffect()` для добавления слушателя для изменений и для очистки слушателей после уничтожения хука.
- Наконец, верните `whenTrue` или `whenFalse` в зависимости от значения `match`.

```jsx
const useMediaQuery = (query, whenTrue, whenFalse) => {
  if (
    typeof window === "undefined" ||
    typeof window.matchMedia === "undefined"
  ) {
    return whenFalse;
  }

  const mediaQuery = window.matchMedia(query);
  const [match, setMatch] = React.useState(!!mediaQuery.matches);

  React.useEffect(() => {
    const handler = () => setMatch(!!mediaQuery.matches);
    mediaQuery.addListener(handler);
    return () => mediaQuery.removeListener(handler);
  }, [mediaQuery]);

  return match ? whenTrue : whenFalse;
};
```

```jsx
const ResponsiveText = () => {
  const text = useMediaQuery(
    "(max - width: 400px)",
    "Less than 400px wide",
    "More than 400px wide"
  );

  return <span>{text}</span>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<ResponsiveText />);
```

Пожалуйста, нажмите на кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб - сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб - страницу.
