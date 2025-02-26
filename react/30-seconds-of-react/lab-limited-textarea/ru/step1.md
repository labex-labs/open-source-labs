# Текстовое поле с ограничением количества символов

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Вот код:

```jsx
const LimitedTextarea = ({ rows, cols, value, limit }) => {
  const [content, setContent] = React.useState(value.slice(0, limit));

  const setFormattedContent = React.useCallback(
    (text) => {
      setContent(text.slice(0, limit));
    },
    [limit]
  );

  return (
    <>
      <textarea
        rows={rows}
        cols={cols}
        onChange={(event) => setFormattedContent(event.target.value)}
        value={content}
      />
      <p>
        {content.length}/{limit}
      </p>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <LimitedTextarea limit={32} value="Hello!" />
);
```

В этом коде мы:

- Упрошили комментарии, чтобы дать более краткое описание того, что делает каждая часть кода.
- Удалили ненужные комментарии кода.
- Удалили функцию `setContent` из массива зависимостей `useCallback`, так как ее там не нужно.
- Добавили круглые скобки вокруг аргумента `text` в функции `useCallback` для согласованности.
- Использовали стрелочные функции для обработчика события `onChange` для краткости.

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
