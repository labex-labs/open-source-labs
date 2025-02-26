# React useOnWindowResize-Hook

> `index.html` und `script.js` wurden bereits in der VM bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Dieser Code führt eine Callback-Funktion aus, jedes Mal wenn das Fenster vergrößert oder verkleinert wird. Um es zu implementieren, sollten Sie die folgenden Schritte befolgen:

1. Erstellen Sie eine Variable namens `listener` mit dem Hook `useRef()`. Diese Variable wird die Referenz auf den Listener speichern.

2. Verwenden Sie den Hook `useEffect()` und `EventTarget.addEventListener()`, um auf das `'resize'`-Ereignis des globalen `Window`-Objekts zu hören. Wenn das Ereignis ausgelöst wird, rufen Sie die `callback`-Funktion auf.

3. Räumen Sie auf, indem Sie alle vorhandenen Listener mit `EventTarget.removeEventListener()` entfernen, wenn die Komponente abmontiert wird.

Hier ist der Code:

```jsx
const useOnWindowResize = (callback) => {
  const listener = React.useRef(null);

  React.useEffect(() => {
    if (listener.current) {
      window.removeEventListener("resize", listener.current);
    }
    listener.current = callback;
    window.addEventListener("resize", callback);
    return () => {
      window.removeEventListener("resize", callback);
    };
  }, [callback]);
};

const App = () => {
  useOnWindowResize(() =>
    console.log(`Fenstergöße: (${window.innerWidth}, ${window.innerHeight})`)
  );
  return (
    <p>
      Vergrößern Sie oder verkleinern Sie das Fenster und überprüfen Sie die
      Konsole.
    </p>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite im Vorschau zu sehen.
