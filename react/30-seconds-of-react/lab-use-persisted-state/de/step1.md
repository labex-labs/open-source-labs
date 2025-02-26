# React usePersistedState-Hook

> `index.html` und `script.js` wurden bereits in der VM bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Dieser Hook gibt einen zustandsbehafteten Wert zurück, der in `localStorage` gespeichert wird, sowie eine Funktion, mit der Sie ihn aktualisieren können. Um ihn zu verwenden, folgen Sie diesen Schritten:

1. Verwenden Sie den `useState()`-Hook, um den `value` auf `defaultValue` zu initialisieren.
2. Verwenden Sie den `useRef()`-Hook, um eine Referenz zu erstellen, die den `name` des Werts in `Window.localStorage` speichern wird.
3. Verwenden Sie 3 Instanzen des `useEffect()`-Hooks für die Initialisierung, die `value`-Änderung und die `name`-Änderung jeweils.
4. Wenn die Komponente zum ersten Mal gerendert wird, verwenden Sie `Storage.getItem()`, um `value` zu aktualisieren, wenn ein gespeicherter Wert vorhanden ist, oder `Storage.setItem()`, um den aktuellen Wert zu speichern.
5. Wenn `value` aktualisiert wird, verwenden Sie `Storage.setItem()`, um den neuen Wert zu speichern.
6. Wenn `name` aktualisiert wird, verwenden Sie `Storage.setItem()`, um den neuen Schlüssel zu erstellen, die `nameRef` zu aktualisieren und `Storage.removeItem()`, um den vorherigen Schlüssel aus `Window.localStorage` zu entfernen.
7. Beachten Sie, dass der Hook für die Verwendung mit primitiven Werten (d.h. nicht Objekten) gedacht ist und Änderungen an `Window.localStorage` aufgrund anderer Code nicht berücksichtigt. Beide dieser Probleme können leicht behoben werden (z.B. JSON-Serialisierung und Behandlung des `'storage'`-Ereignisses).

Hier ist der Code:

```jsx
const usePersistedState = (name, defaultValue) => {
  const [value, setValue] = React.useState(defaultValue);
  const nameRef = React.useRef(name);

  React.useEffect(() => {
    try {
      const storedValue = localStorage.getItem(name);
      if (storedValue !== null) {
        setValue(storedValue);
      } else {
        localStorage.setItem(name, defaultValue);
      }
    } catch {
      setValue(defaultValue);
    }
  }, []);

  React.useEffect(() => {
    try {
      localStorage.setItem(nameRef.current, value);
    } catch {}
  }, [value]);

  React.useEffect(() => {
    const lastName = nameRef.current;
    if (name !== lastName) {
      try {
        localStorage.setItem(name, value);
        nameRef.current = name;
        localStorage.removeItem(lastName);
      } catch {}
    }
  }, [name]);

  return [value, setValue];
};
```

```jsx
const MyComponent = ({ name }) => {
  const [value, setValue] = usePersistedState(name, 10);

  const handleInputChange = (event) => {
    setValue(event.target.value);
  };

  return <input value={value} onChange={handleInputChange} />;
};

const MyApp = () => {
  const [name, setName] = React.useState("my-value");

  const handleInputChange = (event) => {
    setName(event.target.value);
  };

  return (
    <>
      <MyComponent name={name} />
      <input value={name} onChange={handleInputChange} />
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
