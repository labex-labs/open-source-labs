# Хук React useMutationObserver

> Файлы `index.html` и `script.js` уже предоставлены в виртуальной машине (VM). Как правило, вам нужно добавить код только в файлы `script.js` и `style.css`.

Для отслеживания изменений в DOM-дереве можно использовать хук `useMutationObserver`. Вот как он работает:

1. Хук принимает три параметра: `ref`, `callback` и `options`.
2. Внутри хука используется хук `useEffect()`, который зависит от значений `callback` и `options`.
3. Если заданный `ref` инициализирован, создается новый `MutationObserver` и передается в него функция `callback`.
4. Вызывается метод `MutationObserver.observe()` с заданными параметрами `options` для отслеживания изменений в заданном `ref`.
5. Метод `MutationObserver.disconnect()` используется для удаления наблюдателя из `ref` при размонтировании компонента.

Вот код:

```jsx
const useMutationObserver = (
  ref,
  callback,
  options = {
    attributes: true,
    characterData: true,
    childList: true,
    subtree: true
  }
) => {
  React.useEffect(() => {
    if (!ref.current) return;

    const observer = new MutationObserver(callback);
    observer.observe(ref.current, options);

    return () => observer.disconnect();
  }, [callback, options, ref]);
};
```

В компоненте `App` используется хук `useMutationObserver` для отслеживания изменений в элементе `mutationRef`. Функция `incrementMutationCount` передается в качестве `callback`.

```jsx
const App = () => {
  const mutationRef = React.useRef();
  const [mutationCount, setMutationCount] = React.useState(0);

  const incrementMutationCount = React.useCallback(() => {
    setMutationCount((count) => count + 1);
  }, []);

  useMutationObserver(mutationRef, incrementMutationCount);

  const [content, setContent] = React.useState("Hello world");

  return (
    <>
      <label htmlFor="content-input">Edit this to update the text:</label>
      <textarea
        id="content-input"
        style={{ width: "100%" }}
        value={content}
        onChange={(e) => setContent(e.target.value)}
      />
      <div style={{ width: "100%" }} ref={mutationRef}>
        <div
          style={{
            resize: "both",
            overflow: "auto",
            maxWidth: "100%",
            border: "1px solid black"
          }}
        >
          <h2>Resize or change the content:</h2>
          <p>{content}</p>
        </div>
      </div>
      <div>
        <h3>Mutation count {mutationCount}</h3>
      </div>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Нажмите на кнопку 'Go Live' в правом нижнем углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы предварительно просмотреть веб-страницу.
