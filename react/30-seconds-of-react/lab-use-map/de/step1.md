# React useMap-Haken

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

- Der `useMap()`-Hook erstellt ein zustandsbehaftetes `Map`-Objekt und eine Reihe von Funktionen, um es mit React-Hooks zu manipulieren.
- Der `useState()`-Hook initialisiert den `Map`-Zustand mit dem `initialValue`.
- Der `useMemo()`-Hook erstellt eine Reihe von nicht mutierenden Aktionen, die den `map`-Zustandsvariablen mit dem Zustandssteller manipulieren, um jedes Mal ein neues `Map` zu erstellen.
- Der `useMap()`-Hook gibt ein Array zurück, das die `map`-Zustandsvariable und die erstellten `Aktionen` enthält.
- Die `MyApp`-Komponente verwendet den `useMap()`-Hook, um das zustandsbehaftete `Map`-Objekt zu initialisieren und Schaltflächen zum Hinzufügen, Zurücksetzen und Entfernen von Elementen aus der `Map` bereitzustellen.
- Die `JSON.stringify()`-Funktion formatiert das `Map`-Objekt in einen lesbaren JSON-String.

```jsx
const useMap = (initialValue) => {
  const [map, setMap] = React.useState(new Map(initialValue));

  const actions = React.useMemo(
    () => ({
      set: (key, value) =>
        setMap((prevMap) => {
          const nextMap = new Map(prevMap);
          nextMap.set(key, value);
          return nextMap;
        }),
      remove: (key) =>
        setMap((prevMap) => {
          const nextMap = new Map(prevMap);
          nextMap.delete(key);
          return nextMap;
        }),
      clear: () => setMap(new Map())
    }),
    [setMap]
  );

  return [map, actions];
};

const MyApp = () => {
  const [map, { set, remove, clear }] = useMap([["apples", 10]]);

  const handleAdd = () => set(Date.now(), new Date().toJSON());
  const handleReset = () => clear();
  const handleRemove = () => remove("apples");

  return (
    <div>
      <button onClick={handleAdd}>Hinzufügen</button>
      <button onClick={handleReset}>Zurücksetzen</button>
      <button onClick={handleRemove} disabled={!map.has("apples")}>
        Äpfel entfernen
      </button>
      <pre>{JSON.stringify(Object.fromEntries(map), null, 2)}</pre>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
