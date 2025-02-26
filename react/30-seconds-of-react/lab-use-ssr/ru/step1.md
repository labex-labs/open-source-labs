# Хук React useSSR

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Для проверки, выполняется ли код в браузере или на сервере, создайте пользовательский хук, который использует `typeof`, `Window`, `Window.document` и `Document.createElement()` для определения доступности DOM. Используйте хук `useState()` для определения переменной состояния `inBrowser` и хук `useEffect()` для ее обновления и очистки в конце. Используйте хук `useMemo()` для мемоизации возвращаемых значений пользовательского хука.

Вот код:

```jsx
const isDOMavailable = !!(
  typeof window !== "undefined" &&
  window.document &&
  window.document.createElement
);

const useSSR = () => {
  const [inBrowser, setInBrowser] = React.useState(isDOMavailable);

  React.useEffect(() => {
    setInBrowser(isDOMavailable);
    return () => {
      setInBrowser(false);
    };
  }, []);

  const useSSRObject = React.useMemo(
    () => ({
      isBrowser: inBrowser,
      isServer: !inBrowser,
      canUseWorkers: typeof Worker !== "undefined",
      canUseEventListeners: inBrowser && !!window.addEventListener,
      canUseViewport: inBrowser && !!window.screen
    }),
    [inBrowser]
  );

  return useSSRObject;
};

const SSRChecker = (props) => {
  const { isBrowser, isServer } = useSSR();

  return (
    <p>{isBrowser ? "Запускается в браузере" : "Запускается на сервере"}</p>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<SSRChecker />);
```

Пожалуйста, нажмите кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
