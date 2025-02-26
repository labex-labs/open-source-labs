# React useInterval-Hook

> `index.html` und `script.js` wurden bereits in der VM bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Um `setInterval()` auf deklarative Weise zu implementieren, können Sie einen benutzerdefinierten Hook erstellen, der einen `callback` und eine `delay` annimmt. Der erste Schritt besteht darin, den `useRef()`-Hook zu verwenden, um eine `ref` für die Callback-Funktion zu erstellen. Anschließend verwenden Sie einen `useEffect()`-Hook, um das neueste `callback` zu merken, sobald es sich ändert. Schließlich verwenden Sie einen `useEffect()`-Hook, der von `delay` abhängt, um das Intervall einzurichten und aufzuräumen.

Hier ist ein Beispielcodeausschnitt für den benutzerdefinierten Hook:

```jsx
const useInterval = (callback, delay) => {
  const savedCallback = React.useRef();

  React.useEffect(() => {
    savedCallback.current = callback;
  }, [callback]);

  React.useEffect(() => {
    const tick = () => {
      savedCallback.current();
    };
    if (delay !== null) {
      let id = setInterval(tick, delay);
      return () => clearInterval(id);
    }
  }, [delay]);
};
```

Sie können dann diesen benutzerdefinierten Hook in Ihren Komponenten verwenden. Beispielsweise um einen Timer zu erstellen, der alle Sekunden aktualisiert:

```jsx
const Timer = (props) => {
  const [seconds, setSeconds] = React.useState(0);

  useInterval(() => {
    setSeconds(seconds + 1);
  }, 1000);

  return <p>{seconds}</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Timer />);
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
