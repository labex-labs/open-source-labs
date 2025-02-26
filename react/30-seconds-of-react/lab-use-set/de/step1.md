# React useSet-Hook

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Diese Funktion erstellt ein `Set`-Objekt mit einem Zustand und einer Reihe von Funktionen, die den Zustand manipulieren können.

Um diese Funktion zu verwenden:

- Rufen Sie `useState()` und den `Set`-Konstruktor auf, um ein neues `Set` aus dem `initialValue` zu erstellen.
- Verwenden Sie `useMemo()`, um eine Reihe von nicht mutierenden Funktionen zu erstellen, die den `set`-Zustandsvariablen manipulieren können. Verwenden Sie den Zustandssteller, um jedes Mal ein neues `Set` zu erstellen.
- Geben Sie sowohl die `set`-Zustandsvariable als auch die erstellten `actions` zurück.

Hier ist eine Beispielimplementierung dieser Funktion:

```jsx
const useSet = (initialValue) => {
  const [set, setSet] = React.useState(new Set(initialValue));

  const actions = React.useMemo(
    () => ({
      add: (item) => setSet((prevSet) => new Set([...prevSet, item])),
      remove: (item) =>
        setSet((prevSet) => new Set([...prevSet].filter((i) => i !== item))),
      clear: () => setSet(new Set())
    }),
    [setSet]
  );

  return [set, actions];
};
```

Hier ist ein Beispiel für die Verwendung dieser Funktion:

```jsx
const MyApp = () => {
  const [set, { add, remove, clear }] = useSet(new Set(["apples"]));

  return (
    <div>
      <button onClick={() => add(String(Date.now()))}>Hinzufügen</button>
      <button onClick={() => clear()}>Zurücksetzen</button>
      <button onClick={() => remove("apples")} disabled={!set.has("apples")}>
        Äpfel entfernen
      </button>
      <pre>{JSON.stringify([...set], null, 2)}</pre>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
