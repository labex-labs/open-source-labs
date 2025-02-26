# React useEventListener-Hook

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Diese Funktion fügt einen Ereignislistener für den angegebenen Ereignistyp auf dem angegebenen Element hinzu. Um diese Funktion zu verwenden, folgen Sie diesen Schritten:

1. Verwenden Sie den `useRef()`-Hook, um eine Referenz zu erstellen, die den `handler` speichern wird.
2. Verwenden Sie den `useEffect()`-Hook, um den Wert der `savedHandler`-Referenz jedes Mal zu aktualisieren, wenn der `handler` sich ändert.
3. Verwenden Sie den `useEffect()`-Hook, um einen Ereignislistener zum angegebenen Element hinzuzufügen und aufzuräumen, wenn das Element entfernt wird.
4. Lassen Sie das letzte Argument, `el`, weg, um standardmäßig das `Fenster` zu verwenden.

Hier ist der Code:

```jsx
const useEventListener = (type, handler, el = window) => {
  const savedHandler = React.useRef(handler);

  React.useEffect(() => {
    savedHandler.current = handler;
  }, [handler]);

  React.useEffect(() => {
    const listener = (e) => savedHandler.current(e);

    el.addEventListener(type, listener);

    return () => {
      el.removeEventListener(type, listener);
    };
  }, [type, el]);
};
```

Und hier ist ein Beispiel für die Verwendung der `useEventListener()`-Funktion:

```jsx
const MyApp = () => {
  const [coords, setCoords] = React.useState({ x: 0, y: 0 });

  const updateCoords = React.useCallback(
    ({ clientX, clientY }) => {
      setCoords({ x: clientX, y: clientY });
    },
    [setCoords]
  );

  useEventListener("mousemove", updateCoords);

  return (
    <p>
      Mauskoordinaten: {coords.x}, {coords.y}
    </p>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite zu previewen.
