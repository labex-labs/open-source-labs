# React useMediaQuery-Hook

> `index.html` und `script.js` wurden bereits in der VM bereitgestellt. Im Allgemeinen müssen Sie nur Code zu `script.js` und `style.css` hinzufügen.

Diese Funktion überprüft, ob die aktuelle Umgebung einer angegebenen Medienabfrage entspricht und gibt den passenden Wert zurück.

- Überprüfen Sie zunächst, ob `Window` und `Window.matchMedia()` existieren. Wenn nicht (z.B. in einer SSR-Umgebung oder einem nicht unterstützten Browser), geben Sie `whenFalse` zurück.
- Verwenden Sie `Window.matchMedia()`, um die angegebene `query` zu treffen. Kastieren Sie seine `matches`-Eigenschaft zu einem boolean und speichern Sie sie in einer Zustandsvariable, `match`, mithilfe des `useState()`-Hooks.
- Verwenden Sie den `useEffect()`-Hook, um einen Listener für Änderungen hinzuzufügen und die Listener aufzuräumen, nachdem der Hook zerstört wurde.
- Geben Sie schließlich `whenTrue` oder `whenFalse` basierend auf dem Wert von `match` zurück.

```jsx
const useMediaQuery = (query, whenTrue, whenFalse) => {
  if (
    typeof window === "undefined" ||
    typeof window.matchMedia === "undefined"
  ) {
    return whenFalse;
  }

  const mediaQuery = window.matchMedia(query);
  const [match, setMatch] = React.useState(!!mediaQuery.matches);

  React.useEffect(() => {
    const handler = () => setMatch(!!mediaQuery.matches);
    mediaQuery.addListener(handler);
    return () => mediaQuery.removeListener(handler);
  }, [mediaQuery]);

  return match ? whenTrue : whenFalse;
};
```

```jsx
const ResponsiveText = () => {
  const text = useMediaQuery(
    "(max-width: 400px)",
    "Kleiner als 400px breit",
    "Größer als 400px breit"
  );

  return <span>{text}</span>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<ResponsiveText />);
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
