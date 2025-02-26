# React useDelayedState-Hook

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Um die Erstellung eines zustandsbehafteten Werts bis eine Bedingung erfüllt ist zu verzögern, folgen Sie diesen Schritten:

1. Verwenden Sie den `useState()`-Hook, um einen zustandsbehafteten Wert zu erstellen, der den tatsächlichen `Zustand` und einen booleschen Wert `geladen` enthält.
2. Verwenden Sie den `useEffect()`-Hook, um den zustandsbehafteten Wert zu aktualisieren, wenn sich die `Bedingung` oder `geladen` ändert.
3. Erstellen Sie eine Funktion `updateState`, die nur den `Zustand`-Wert aktualisiert, wenn `geladen` wahr ist.

```jsx
const useDelayedState = (initialState, condition) => {
  const [{ state, loaded }, setState] = React.useState({
    state: null,
    loaded: false
  });

  React.useEffect(() => {
    if (!loaded && condition) setState({ state: initialState, loaded: true });
  }, [condition, loaded]);

  const updateState = (newState) => {
    if (!loaded) return;
    setState({ state: newState, loaded });
  };

  return [state, updateState];
};
```

Hier ist ein Beispiel dafür, wie der `useDelayedState`-Hook verwendet werden kann:

```jsx
const App = () => {
  const [branches, setBranches] = React.useState([]);
  const [selectedBranch, setSelectedBranch] = useDelayedState(
    branches[0],
    branches.length
  );

  React.useEffect(() => {
    const handle = setTimeout(() => {
      setBranches(["master", "staging", "test", "dev"]);
    }, 2000);
    return () => {
      handle && clearTimeout(handle);
    };
  }, []);

  return (
    <div>
      <p>Ausgewählter Zweig: {selectedBranch}</p>
      <select onChange={(e) => setSelectedBranch(e.target.value)}>
        {branches.map((branch) => (
          <option key={branch} value={branch}>
            {branch}
          </option>
        ))}
      </select>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
