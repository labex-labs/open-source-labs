# React useTimeout-Hook

> `index.html` und `script.js` wurden bereits in der VM bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Um `setTimeout()` auf deklarative Weise zu implementieren, erstellen Sie einen benutzerdefinierten Hook, der einen `callback` und eine `delay` annimmt. Verwenden Sie den `useRef()`-Hook, um eine `ref` für die Callback-Funktion zu erstellen, und verwenden Sie den `useEffect()`-Hook, um die neueste Callback-Funktion zu merken. Anschließend verwenden Sie den `useEffect()`-Hook, um den Zeitüberschuss einzurichten und aufzuräumen.

Hier ist ein Beispielcodeausschnitt, der diesen Ansatz demonstriert:

```jsx
const useTimeout = (callback, delay) => {
  const savedCallback = React.useRef();

  React.useEffect(() => {
    savedCallback.current = callback;
  }, [callback]);

  React.useEffect(() => {
    const tick = () => {
      savedCallback.current();
    };
    if (delay !== null) {
      let id = setTimeout(tick, delay);
      return () => clearTimeout(id);
    }
  }, [delay]);
};

const OneSecondTimer = (props) => {
  const [seconds, setSeconds] = React.useState(0);

  useTimeout(() => {
    setSeconds(seconds + 1);
  }, 1000);

  return <p>{seconds}</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<OneSecondTimer />);
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
