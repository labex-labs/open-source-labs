# React useUnload-Hook

> `index.html` und `script.js` wurden bereits in der virtuellen Maschine (VM) bereitgestellt. Im Allgemeinen müssen Sie nur Code zu `script.js` und `style.css` hinzufügen.

Das `beforeunload`-Fensterereignis (window event) kann mit folgenden Schritten behandelt werden:

1. Erstellen Sie eine Referenz (ref) für die Callback-Funktion `fn` mithilfe des `useRef()`-Hooks.
2. Verwenden Sie den `useEffect()`-Hook und `EventTarget.addEventListener()`, um das `'beforeunload'`-Ereignis zu behandeln, das ausgelöst wird, wenn der Benutzer das Fenster schließen möchte.
3. Verwenden Sie `EventTarget.removeEventListener()`, um die Bereinigung (cleanup) nach dem Entfernen der Komponente (unmounting) durchzuführen.

Hier ist der Code:

```jsx
const useUnload = (fn) => {
  const callbackRef = React.useRef(fn);

  React.useEffect(() => {
    const callback = callbackRef.current;
    window.addEventListener("beforeunload", callback);
    return () => {
      window.removeEventListener("beforeunload", callback);
    };
  }, [callbackRef]);
};

const App = () => {
  useUnload((e) => {
    e.preventDefault();
    const exit = confirm("Are you sure you want to leave?");
    if (exit) window.close();
  });

  return <div>Try closing the window.</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Klicken Sie bitte auf 'Go Live' in der unteren rechten Ecke, um den Web-Service auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzusehen.
