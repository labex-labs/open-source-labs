# React useWindowSize-Hook

> `index.html` und `script.js` wurden bereits in der VM bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Um die Abmessungen des Browserfensters zu verfolgen, können die folgenden Schritte durchgeführt werden:

1. Verwenden Sie den `useState()`-Hook, um eine Zustandsvariable `windowSize` zu initialisieren, die die Fensterabmessungen aufnehmen wird. Initialisieren Sie beide Werte mit `undefined`, um eine Inkonsistenz zwischen Server- und Client-Rendern zu vermeiden.

```jsx
const [windowSize, setWindowSize] = React.useState({
  width: undefined,
  height: undefined
});
```

2. Erstellen Sie eine Funktion `handleResize()`, die `Window.innerWidth` und `Window.innerHeight` verwendet, um die Zustandsvariable zu aktualisieren. Diese Funktion wird jedes Mal aufgerufen, wenn das Ereignis `'resize'` ausgelöst wird.

```jsx
const handleResize = () =>
  setWindowSize({ width: window.innerWidth, height: window.innerHeight });
```

3. Verwenden Sie den `useEffect()`-Hook, um einen passenden Listener für das Ereignis `'resize'` beim Mount festzulegen und ihn beim Entfernen aufzuräumen.

```jsx
React.useEffect(() => {
  window.addEventListener("resize", handleResize);

  handleResize();

  return () => {
    window.removeEventListener("resize", handleResize);
  };
}, []);
```

Wenn man das alles zusammenfasst, kann der benutzerdefinierte Hook `useWindowSize()` wie folgt definiert werden:

```jsx
const useWindowSize = () => {
  const [windowSize, setWindowSize] = React.useState({
    width: undefined,
    height: undefined
  });

  const handleResize = () =>
    setWindowSize({ width: window.innerWidth, height: window.innerHeight });

  React.useEffect(() => {
    window.addEventListener("resize", handleResize);

    handleResize();

    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []);

  return windowSize;
};
```

Um den `useWindowSize()`-Hook zu verwenden, rufen Sie ihn einfach in einer Komponente auf und extrahieren Sie die `width`- und `height`-Werte aus dem zurückgegebenen Objekt.

```jsx
const MyApp = () => {
  const { width, height } = useWindowSize();

  return (
    <p>
      Fenstergröße: ({width} x {height})
    </p>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
