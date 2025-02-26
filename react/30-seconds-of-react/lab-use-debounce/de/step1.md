# React useDebounce-Hook

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Um einen gegebenen Wert zu debouncen, können Sie einen benutzerdefinierten Hook erstellen, der einen `value` und eine `delay` annimmt. Verwenden Sie den `useState()`-Hook, um den debouncen-Wert zu speichern, und den `useEffect()`-Hook, um den debouncen-Wert jedes Mal zu aktualisieren, wenn `value` aktualisiert wird. Um das Aufrufen des Setters der vorherigen Zustandsvariablen um `delay` ms zu verzögern, verwenden Sie `setTimeout()`. Um aufzuräumen, wenn die Komponente abgebaut wird, verwenden Sie `clearTimeout()`. Dies ist besonders nützlich, wenn es um Benutzereingaben geht.

Hier ist eine Beispielimplementierung des `useDebounce()`-Hooks:

```jsx
const useDebounce = (value, delay) => {
  const [debouncedValue, setDebouncedValue] = React.useState(value);

  React.useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    return () => {
      clearTimeout(handler);
    };
  }, [value, delay]);

  return debouncedValue;
};
```

Sie können den `useDebounce()`-Hook in einer Komponente wie folgt verwenden:

```jsx
const Counter = () => {
  const [value, setValue] = React.useState(0);
  const lastValue = useDebounce(value, 500);

  return (
    <div>
      <p>
        Aktuell: {value} - Debouncen: {lastValue}
      </p>
      <button onClick={() => setValue(value + 1)}>Inkrementieren</button>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Counter />);
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
