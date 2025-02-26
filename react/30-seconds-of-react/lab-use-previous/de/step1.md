# React usePrevious-Hook

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Um den vorherigen Zustand oder die vorherigen Props zu speichern, können Sie einen benutzerdefinierten Hook erstellen. Hier sind die Schritte:

1. Definieren Sie einen benutzerdefinierten Hook, der ein `value`-Argument akzeptiert.
2. Verwenden Sie den `useRef()`-Hook, um eine `ref` für den `value` zu erstellen.
3. Verwenden Sie den `useEffect()`-Hook, um den neuesten `value` zu merken.
4. Geben Sie den `ref.current`-Wert zurück.

```jsx
const usePrevious = (value) => {
  const ref = React.useRef();
  React.useEffect(() => {
    ref.current = value;
  });
  return ref.current;
};
```

Hier ist ein Beispiel für die Verwendung des `usePrevious`-Hooks:

```jsx
const Counter = () => {
  const [value, setValue] = React.useState(0);
  const lastValue = usePrevious(value);

  return (
    <div>
      <p>
        Aktuell: {value} - Vorheriges: {lastValue}
      </p>
      <button onClick={() => setValue(value + 1)}>Inkrementieren</button>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Counter />);
```

Der `Counter`-Component zeigt den aktuellen und den vorherigen Wert von `value` an. Wenn der `Inkrementieren`-Button geklickt wird, wird `value` aktualisiert und der vorherige Wert wird mithilfe des `usePrevious`-Hooks gespeichert.

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
