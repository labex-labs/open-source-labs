# React useOnGlobalEvent-Hook

> `index.html` und `script.js` wurden bereits in der VM bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Diese Funktion führt eine Callback-Funktion aus, wenn ein Ereignis auf dem globalen Objekt auftritt. Um diese Funktion zu implementieren:

1. Verwenden Sie den `useRef()`-Hook, um eine Variable `listener` zu erstellen, die die Listenerreferenz aufnehmen wird.
2. Verwenden Sie den `useRef()`-Hook, um eine Variable zu erstellen, die die vorherigen Werte der `type`- und `options`-Argumente aufnehmen wird.
3. Verwenden Sie den `useEffect()`-Hook und `EventTarget.addEventListener()`, um auf das gegebene Ereignis `type` auf dem globalen `Window`-Objekt zu lauschen.
4. Verwenden Sie `EventTarget.removeEventListener()`, um alle vorhandenen Listener zu entfernen und aufzuräumen, wenn die Komponente abmontiert wird.

```jsx
const useOnGlobalEvent = (type, callback, options) => {
  const listener = React.useRef(null);
  const previousProps = React.useRef({ type, options });

  React.useEffect(() => {
    const { type: previousType, options: previousOptions } =
      previousProps.current;

    if (listener.current) {
      window.removeEventListener(
        previousType,
        listener.current,
        previousOptions
      );
    }

    listener.current = callback;
    window.addEventListener(type, callback, options);
    previousProps.current = { type, options };

    return () => {
      window.removeEventListener(type, listener.current, options);
    };
  }, [callback, type, options]);
};
```

Hier ist ein Beispiel, wie diese Funktion verwendet werden kann:

```jsx
const App = () => {
  useOnGlobalEvent("mousemove", (e) => {
    console.log(`(${e.x}, ${e.y})`);
  });

  return <p>Move your mouse around</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
