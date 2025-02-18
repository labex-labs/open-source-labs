# React useError-Hook

> `index.html` und `script.js` wurden bereits in der virtuellen Maschine (VM) bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Dieser Code erstellt einen Fehler-Dispatcher (Error Dispatcher). Er verwendet drei React-Hooks, um den Fehlerzustand (error state) zu verwalten und ihn an die Benutzeroberfläche zu übermitteln.

So funktioniert der Code:

1. Der `useState()`-Hook erstellt eine Zustandsvariable (state variable) namens `error`, die das Fehlerobjekt enthält. Er nimmt einen Anfangswert von `err` an, der als Argument an den Hook übergeben wird.

2. Der `useEffect()`-Hook wird verwendet, um den Fehler auszulösen, sobald er einen wahrheitsgemäßen Wert hat. Dieser Hook nimmt eine Funktion und ein Array von Abhängigkeiten als Argumente. In diesem Fall überprüft die Funktion, ob die Zustandsvariable `error` einen wahrheitsgemäßen Wert hat (d. h. nicht null, undefined, 0, false oder eine leere Zeichenkette ist) und löst ihn aus, wenn dies der Fall ist. Das Array der Abhängigkeiten ist `[error]`, was bedeutet, dass der Effekt erneut ausgeführt wird, sobald sich die Variable `error` ändert.

3. Der `useCallback()`-Hook wird verwendet, um eine zwischengespeicherte Funktion namens `dispatchError` zu erstellen, die die Zustandsvariable `error` aktualisiert und die neue Funktion zurückgibt. Dieser Hook nimmt eine Funktion und ein Array von Abhängigkeiten als Argumente. In diesem Fall nimmt die Funktion ein Argument `err` an, das das neue Fehlerobjekt ist, das übermittelt werden soll. Das Array der Abhängigkeiten ist `[]`, was bedeutet, dass die zwischengespeicherte Funktion nur neu erstellt wird, wenn die Komponente neu gerendert wird.

Hier ist ein Beispiel, wie man den `useError()`-Hook in einer Komponente verwendet:

1. Erstellen Sie eine neue Komponente namens `ErrorButton`.

2. Rufen Sie innerhalb der Komponente den `useError()`-Hook auf, um die `dispatchError`-Funktion zu erhalten.

3. Erstellen Sie eine Klick-Handler-Funktion namens `clickHandler`, die `dispatchError` mit einem neuen Fehlerobjekt aufruft.

4. Rendern Sie einen Button, der `clickHandler` aufruft, wenn er geklickt wird.

Hier ist der Code:

```jsx
const useError = (err = null) => {
  const [error, setError] = React.useState(err);

  React.useEffect(() => {
    if (error) {
      throw error;
    }
  }, [error]);

  const dispatchError = React.useCallback((err) => {
    setError(err);
  }, []);

  return dispatchError;
};

const ErrorButton = () => {
  const dispatchError = useError();

  const clickHandler = () => {
    dispatchError(new Error("Error!"));
  };

  return <button onClick={clickHandler}>Throw error</button>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<ErrorButton />);
```

Klicken Sie bitte auf 'Go Live' in der unteren rechten Ecke, um den Web-Service auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzusehen.
