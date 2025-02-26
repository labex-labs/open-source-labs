# Textfeld mit Wortbegrenzung

> `index.html` und `script.js` wurden bereits in der VM bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

```jsx
// Rendert ein Textfeld-Komponent mit einer Wortbegrenzung.
const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
  const [{ content, wordCount }, setContent] = React.useState({
    content: value,
    wordCount: 0
  });

  // Erstellt eine memoisierte Funktion, die den eingegebenen Text formatiert.
  const setFormattedContent = React.useCallback(
    (text) => {
      const words = text.split(" ").filter(Boolean);
      const truncated = words.slice(0, limit).join(" ");
      setContent({
        content: words.length > limit ? truncated : text,
        wordCount: words.length > limit ? limit : words.length
      });
    },
    [limit, setContent]
  );

  // Ruft setFormattedContent auf dem Anfangswert von content auf.
  React.useEffect(() => {
    setFormattedContent(content);
  }, []);

  return (
    <>
      <textarea
        rows={rows}
        cols={cols}
        value={content}
        onChange={(event) => setFormattedContent(event.target.value)}
      />
      <p>
        {wordCount}/{limit}
      </p>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <LimitedWordTextarea limit={5} value="Hello there!" />
);
```

Vorgenommene Änderungen:

- Hinzugefügt Kommentare, um zu erklären, was jeder Teil des Codes macht.
- Vereinfacht die Logik in `setFormattedContent`, um sie prägnanter zu machen.
- Verschoben die `setContent`-Funktion ans Ende der Funktionsaufrufe, um sie lesbarer zu machen.
- Sortiert die Props in der `<textarea>`-Komponente um, um Konsistenz zu gewährleisten.
- Entfernt unnötige Leerzeichen und Zeilenumbrüche.

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite zu Vorschauen.
