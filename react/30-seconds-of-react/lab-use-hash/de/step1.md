# React useHash-Hook

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Dieser Code verfolgt und aktualisiert den Hash-Wert der Browser-Adresse. Um ihn zu verwenden, folgen Sie diesen Schritten:

1. Verwenden Sie den `useState()`-Hook, um die `hash`-Eigenschaft des `Location`-Objekts träge zu erhalten.
2. Verwenden Sie den `useCallback()`-Hook, um einen Handler zu erstellen, der den `hash`-Zustand aktualisiert, wenn das Ereignis `'hashchange'` ausgelöst wird.
3. Verwenden Sie den `useEffect()`-Hook, um einen Listener für das Ereignis `'hashchange'` beim Mounten hinzuzufügen und ihn beim Entfernen zu bereinigen.
4. Verwenden Sie den `useCallback()`-Hook, um eine Funktion zu erstellen, die die `hash`-Eigenschaft des `Location`-Objekts mit dem angegebenen Wert aktualisiert.
5. In Ihrer Komponente rufen Sie `useHash()` auf, um den aktuellen `hash`-Wert und eine `updateHash()`-Funktion zu erhalten, um ihn zu ändern.
6. Verwenden Sie die `updateHash()`-Funktion, um den `hash`-Wert zu ändern.
7. Rendern Sie den aktuellen `hash`-Wert in einer Komponente.
8. Erstellen Sie ein Eingabefeld, das es dem Benutzer ermöglicht, den `hash`-Wert zu ändern.

Hier ist der Code:

```jsx
const useHash = () => {
  const [hash, setHash] = React.useState(() => window.location.hash);

  const hashChangeHandler = React.useCallback(() => {
    setHash(window.location.hash);
  }, []);

  React.useEffect(() => {
    window.addEventListener("hashchange", hashChangeHandler);
    return () => {
      window.removeEventListener("hashchange", hashChangeHandler);
    };
  }, []);

  const updateHash = React.useCallback(
    (newHash) => {
      if (newHash !== hash) window.location.hash = newHash;
    },
    [hash]
  );

  return [hash, updateHash];
};

const MyApp = () => {
  const [hash, setHash] = useHash();

  React.useEffect(() => {
    setHash("#list");
  }, []);

  return (
    <>
      <p>Aktueller Hash-Wert: {hash}</p>
      <p>Hash bearbeiten: </p>
      <input value={hash} onChange={(e) => setHash(e.target.value)} />
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite zu previewen.
