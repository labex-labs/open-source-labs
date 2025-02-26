# React useSessionStorage-Hook

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Um einen zustandsbezogenen Wert zu erstellen, der in den `sessionStorage` gespeichert wird, und eine Funktion zum Aktualisieren desselben, folgen Sie diesen Schritten:

1. Verwenden Sie den `useState()`-Hook mit einer Funktion, um seinen Wert träge zu initialisieren.
2. Verwenden Sie einen `try...catch`-Block und `Storage.getItem()`, um versuchen, den Wert aus `Window.sessionStorage` zu erhalten. Wenn kein Wert gefunden wird, verwenden Sie `Storage.setItem()`, um den `defaultValue` zu speichern und ihn als Initialzustand zu verwenden. Wenn ein Fehler auftritt, verwenden Sie `defaultValue` als Initialzustand.
3. Definieren Sie eine Funktion, die die Zustandsvariable mit dem übergebenen Wert aktualisiert und `Storage.setItem()` verwendet, um ihn zu speichern.

Hier ist eine Beispielimplementierung:

```jsx
const useSessionStorage = (keyName, defaultValue) => {
  const [storedValue, setStoredValue] = React.useState(() => {
    try {
      const value = window.sessionStorage.getItem(keyName);

      if (value) {
        return JSON.parse(value);
      } else {
        window.sessionStorage.setItem(keyName, JSON.stringify(defaultValue));
        return defaultValue;
      }
    } catch (err) {
      return defaultValue;
    }
  });

  const setValue = (newValue) => {
    try {
      window.sessionStorage.setItem(keyName, JSON.stringify(newValue));
    } catch (err) {}
    setStoredValue(newValue);
  };

  return [storedValue, setValue];
};
```

Sie können diesen Hook in Ihrer App wie folgt verwenden:

```jsx
const MyApp = () => {
  const [name, setName] = useSessionStorage("name", "John");

  return <input value={name} onChange={(e) => setName(e.target.value)} />;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
