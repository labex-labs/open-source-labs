# React useSSR-Hook

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Um zu überprüfen, ob der Code im Browser oder auf dem Server ausgeführt wird, erstellen Sie einen benutzerdefinierten Hook, der `typeof`, `Window`, `Window.document` und `Document.createElement()` verwendet, um zu bestimmen, ob das DOM verfügbar ist. Verwenden Sie den `useState()`-Hook, um die `inBrowser`-Zustandsvariable zu definieren, und den `useEffect()`-Hook, um sie zu aktualisieren und am Ende aufzuräumen. Verwenden Sie den `useMemo()`-Hook, um die Rückgabewerte des benutzerdefinierten Hooks zu memoisiert.

Hier ist der Code:

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
    <p>{isBrowser ? "Im Browser ausgeführt" : "Auf dem Server ausgeführt"}</p>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<SSRChecker />);
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
