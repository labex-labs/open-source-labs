# Хук useCopyToClipboard в React

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Для копирования заданного текста в буфер обмена используйте сниппет `copyToClipboard`, предоставленный в `/js/s/copy-to-clipboard/`, вместе с хуком `useState()` для инициализации переменной `copied`. Чтобы создать обратный вызов для метода `copyToClipboard`, используйте хук `useCallback()`. Чтобы сбросить переменную состояния `copied`, когда меняется `text`, используйте хук `useEffect()`. Наконец, верните переменную состояния `copied` и обратный вызов `copy`.

Следующий код демонстрирует пример использования этих хуков и методов для создания компонента `TextCopy`. Когда пользователь нажимает кнопку "Нажмите, чтобы скопировать", вызывается функция `copy` и переменная `copied` устанавливается в `true`. Если копирование прошло успешно, будет отображено "Скопировано!".

```jsx
const useCopyToClipboard = (text) => {
  const copyToClipboard = (str) => {
    const el = document.createElement("textarea");
    el.value = str;
    el.setAttribute("readonly", "");
    el.style.position = "absolute";
    el.style.left = "-9999px";
    document.body.appendChild(el);
    const selected =
      document.getSelection().rangeCount > 0
        ? document.getSelection().getRangeAt(0)
        : false;
    el.select();
    const success = document.execCommand("copy");
    document.body.removeChild(el);
    if (selected) {
      document.getSelection().removeAllRanges();
      document.getSelection().addRange(selected);
    }
    return success;
  };

  const [copied, setCopied] = React.useState(false);

  const copy = React.useCallback(() => {
    if (!copied) setCopied(copyToClipboard(text));
  }, [text]);

  React.useEffect(() => () => setCopied(false), [text]);

  return [copied, copy];
};

const TextCopy = (props) => {
  const [copied, copy] = useCopyToClipboard("Lorem ipsum");

  return (
    <div>
      <button onClick={copy}>Click to copy</button>
      <span>{copied && "Copied!"}</span>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<TextCopy />);
```

Пожалуйста, нажмите на кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
