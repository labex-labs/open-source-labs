# Текстовое поле с ограничением по количеству слов

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

```jsx
// Отображает компонент текстового поля с ограничением по количеству слов.
const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
  const [{ content, wordCount }, setContent] = React.useState({
    content: value,
    wordCount: 0
  });

  // Создает мемоизированную функцию, которая форматирует вводимый текст.
  const setFormattedContent = React.useCallback(
    (text) => {
      const words = text.split(" ").filter(Boolean);
      const truncated = words.slice(0, limit).join(" ");
      setContent({
        content: words.length > limit ? truncated : text,
        wordCount: words.length > limit ? limit : words.length
      });
    },
    [limit, setContent]
  );

  // Вызывает setFormattedContent для начального значения content.
  React.useEffect(() => {
    setFormattedContent(content);
  }, []);

  return (
    <>
      <textarea
        rows={rows}
        cols={cols}
        value={content}
        onChange={(event) => setFormattedContent(event.target.value)}
      />
      <p>
        {wordCount}/{limit}
      </p>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <LimitedWordTextarea limit={5} value="Hello there!" />
);
```

Внесенные изменения:

- Добавлены комментарии для объяснения того, что делает каждая часть кода.
- Упрощен логика в `setFormattedContent`, чтобы сделать ее более компактной.
- Перемещено функцию `setContent` в конец вызова функции, чтобы сделать ее легче читать.
- Переупорядочены свойства в компоненте `<textarea>` для согласованности.
- Удалены лишние пробелы и переносы строк.

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем можно обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
