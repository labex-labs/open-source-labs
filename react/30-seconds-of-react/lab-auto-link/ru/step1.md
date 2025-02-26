# Автоматическое текстовое связывание

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Данный компонент отображает строку в виде простого текста, при этом URL-адреса преобразуются в соответствующие элементы гиперссылок.

Для этого он использует `String.prototype.split()` и `String.prototype.match()` с регулярным выражением для поиска URL-адресов в заданной строке. Найденные URL-адресы возвращаются в виде элементов `<a>`, обрабатывая при необходимости отсутствие префикса протокола. Оставшиеся части строки отображаются в виде простого текста.

Вот код:

```jsx
const AutoLink = ({ text }) => {
  const urlRegex =
    /((?:https?:\/\/)?(?:(?:[a-z0-9]?(?:[a-z0-9\-]{1,61}[a-z0-9])?\.[^\.|\s])+[a-z\.]*[a-z]+|(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3})(?::\d{1,5})*[a-z0-9.,_\/~#&=;%+?\-\\(\\)]*)/gi;

  const renderText = () => {
    return text.split(urlRegex).map((word, index) => {
      const urlMatch = word.match(urlRegex);
      if (urlMatch) {
        const url = urlMatch[0];
        return (
          <a key={index} href={url.startsWith("http") ? url : `http://${url}`}>
            {url}
          </a>
        );
      }
      return <span key={index}>{word}</span>;
    });
  };

  return <div>{renderText()}</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <AutoLink text="foo bar baz http://example.org bar" />
);
```

Пожалуйста, нажмите кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
