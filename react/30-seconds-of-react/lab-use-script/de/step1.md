# React useScript-Hook

> `index.html` und `script.js` wurden bereits in der VM bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Um ein externes Skript dynamisch zu laden, verwenden Sie den `useState()`-Hook, um eine Zustandsvariable zu erstellen, die den Ladezustand des Skripts speichert. Anschließend verwenden Sie den `useEffect()`-Hook, um alle Logik für das Laden und Entladen des Skripts jederzeit zu behandeln, wenn sich der `src` ändert. Wenn kein `src`-Wert vorhanden ist, legen Sie den `status` auf `'idle'` fest und geben Sie zurück. Verwenden Sie `Document.querySelector()`, um zu überprüfen, ob ein `<script>`-Element mit dem entsprechenden `src`-Wert existiert. Wenn kein relevantes Element existiert, verwenden Sie `Document.createElement()`, um eines zu erstellen und ihm die entsprechenden Attribute zu geben. Verwenden Sie das `data-status`-Attribut, um den Status des Skripts anzuzeigen und setzen Sie es zunächst auf `'loading'`. Wenn ein relevantes Element existiert, überspringen Sie die Initialisierung und aktualisieren Sie den `status` aus seinem `data-status`-Attribut. Dadurch wird sichergestellt, dass kein doppeltes Element erstellt wird. Verwenden Sie `EventTarget.addEventListener()`, um auf `'load'`- und `'error'`-Ereignisse zu hören und verarbeiten Sie sie, indem Sie das `data-status`-Attribut und die `status`-Zustandsvariable aktualisieren. Schließlich, wenn die Komponente abgebaut wird, verwenden Sie `Document.removeEventListener()`, um alle Listener, die an das Element gebunden sind, zu entfernen.

Hier ist eine Beispielimplementierung des `useScript`-Hooks:

```jsx
const useScript = (src) => {
  const [status, setStatus] = React.useState(src ? "loading" : "idle");

  React.useEffect(() => {
    if (!src) {
      setStatus("idle");
      return;
    }

    let script = document.querySelector(`script[src="${src}"]`);

    if (!script) {
      script = document.createElement("script");
      script.src = src;
      script.async = true;
      script.setAttribute("data-status", "loading");
      document.body.appendChild(script);

      const setDataStatus = (event) => {
        script.setAttribute(
          "data-status",
          event.type === "load" ? "ready" : "error"
        );
      };
      script.addEventListener("load", setDataStatus);
      script.addEventListener("error", setDataStatus);
    } else {
      setStatus(script.getAttribute("data-status"));
    }

    const setStateStatus = (event) => {
      setStatus(event.type === "load" ? "ready" : "error");
    };

    script.addEventListener("load", setStateStatus);
    script.addEventListener("error", setStateStatus);

    return () => {
      if (script) {
        script.removeEventListener("load", setStateStatus);
        script.removeEventListener("error", setStateStatus);
      }
    };
  }, [src]);

  return status;
};
```

Hier ist ein Beispiel für die Verwendung des `useScript`-Hooks:

```jsx
const script =
  "data:text/plain;charset=utf-8;base64,KGZ1bmN0aW9uKCl7IGNvbnNvbGUubG9nKCdIZWxsbycpIH0pKCk7";

const Child = () => {
  const status = useScript(script);
  return <p>Child status: {status}</p>;
};

const MyApp = () => {
  const status = useScript(script);
  return (
    <>
      <p>Parent status: {status}</p>
      <Child />
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
