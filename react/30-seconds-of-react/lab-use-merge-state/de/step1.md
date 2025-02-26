# React useMergeState-Hook

> `index.html` und `script.js` wurden bereits in der VM bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Um einen zustandsbehafteten Wert und eine Funktion zu erstellen, um ihn durch Zusammenführen des bereitgestellten neuen Zustands zu aktualisieren, verwenden Sie den `useState()`-Hook, um eine Zustandsvariable zu erstellen und sie mit `initialState` zu initialisieren. Erstellen Sie eine Funktion, die die Zustandsvariable aktualisiert, indem sie den bereitgestellten neuen Zustand mit dem bestehenden zusammenführt. Wenn der neue Zustand eine Funktion ist, rufen Sie sie mit dem vorherigen Zustand als Argument auf und verwenden das Ergebnis. Wenn kein Argument angegeben wird, wird die Zustandsvariable mit einem leeren Objekt (`{}`) initialisiert. Der folgende Code zeigt, wie dies mithilfe des benutzerdefinierten `useMergeState`-Hooks implementiert wird:

```jsx
const useMergeState = (initialState = {}) => {
  const [value, setValue] = React.useState(initialState);

  const mergeState = (newState) => {
    if (typeof newState === "function") {
      newState = newState(value);
    }
    setValue({ ...value, ...newState });
  };

  return [value, mergeState];
};
```

Hier ist ein Beispiel für die Verwendung des `useMergeState`-Hooks in einem Komponenten namens `MyApp`:

```jsx
const MyApp = () => {
  const [data, setData] = useMergeState({ name: "John", age: 20 });

  return (
    <>
      <input
        value={data.name}
        onChange={(e) => setData({ name: e.target.value })}
      />
      <button onClick={() => setData(({ age }) => ({ age: age - 1 }))}>
        -
      </button>
      {data.age}
      <button onClick={() => setData(({ age }) => ({ age: age + 1 }))}>
        +
      </button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
