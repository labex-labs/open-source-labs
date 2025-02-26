# React useDefault Hook

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Hier ist der Code:

```jsx
const useDefault = (defaultState, initialState) => {
  const [value, setValue] = React.useState(initialState);
  const isEmpty = value === undefined || value === null;
  return [isEmpty ? defaultState : value, setValue];
};
```

```jsx
const UserCard = () => {
  const [user, setUser] = useDefault({ name: "Adam" }, { name: "John" });

  return (
    <>
      <div>User: {user.name}</div>
      <input onChange={(e) => setUser({ name: e.target.value })} />
      <button onClick={() => setUser(null)}>Clear</button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<UserCard />);
```

Um einen zustandsbehafteten Wert mit einem Standardwert als Rückfall zu erstellen, verwenden Sie den `useState()`-Hook in React. Überprüfen Sie, ob der Anfangswert entweder `null` oder `undefined` ist. Wenn ja, geben Sie stattdessen den `defaultState` zurück, andernfalls geben Sie den tatsächlichen `value`-Zustand und die `setValue`-Funktion zurück. Der obige Code zeigt, wie diese Funktionalität in einem benutzerdefinierten Hook namens `useDefault` implementiert wird.

Im bereitgestellten Beispiel wird `useDefault` verwendet, um einen `user`-Zustand mit einem Standardwert von `{ name: 'Adam' }` zu erstellen. Der Anfangszustand wird auf `{ name: 'John' }` gesetzt. Im `UserCard`-Komponenten wird `user` zusammen mit einem Eingabefeld angezeigt, um seinen Namen zu aktualisieren. Es wird auch eine Leer-Button bereitgestellt, um den Zustand zurückzusetzen auf `null`. Schließlich wird die Komponente mithilfe von `ReactDOM.createRoot()` gerendert.

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
