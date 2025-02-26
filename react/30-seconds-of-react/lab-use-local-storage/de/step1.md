# React useLocalStorage-Hook

> `index.html` und `script.js` wurden bereits in der VM bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Diese Funktion erstellt einen Wert, der in den `localStorage` gespeichert wird, und eine Funktion, um ihn zu modifizieren. So funktioniert es:

1. Um den Wert zu erstellen, verwenden Sie den `useState()`-Hook mit einer Funktion, um ihn träge zu initialisieren.
2. Um den gespeicherten Wert aus dem `localStorage` abzurufen, verwenden Sie einen `try...catch`-Block und `Storage.getItem()`. Wenn kein gespeicherter Wert vorhanden ist, verwenden Sie `Storage.setItem()`, um den `defaultValue` zu speichern und ihn als Initialzustand zu verwenden. Wenn ein Fehler auftritt, verwenden Sie `defaultValue`.
3. Definieren Sie eine Funktion, die die Zustandsvariable mit dem übergebenen Wert aktualisiert und `Storage.setItem()` verwendet, um ihn zu speichern.

Hier ist der Code:

```jsx
const useLocalStorage = (keyName, defaultValue) => {
  const [storedValue, setStoredValue] = React.useState(() => {
    try {
      const value = window.localStorage.getItem(keyName);

      if (value) {
        return JSON.parse(value);
      } else {
        window.localStorage.setItem(keyName, JSON.stringify(defaultValue));
        return defaultValue;
      }
    } catch (err) {
      return defaultValue;
    }
  });

  const setValue = (newValue) => {
    try {
      window.localStorage.setItem(keyName, JSON.stringify(newValue));
    } catch (err) {}
    setStoredValue(newValue);
  };

  return [storedValue, setValue];
};
```

Sie können diese Funktion in Ihrer App wie folgt verwenden:

```jsx
const MyApp = () => {
  const [name, setName] = useLocalStorage("name", "John");

  return <input value={name} onChange={(e) => setName(e.target.value)} />;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
