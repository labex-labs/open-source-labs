# Textbereich mit Zeichenbegrenzung

> `index.html` und `script.js` wurden bereits in der VM bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Hier ist der Code:

```jsx
const LimitedTextarea = ({ rows, cols, value, limit }) => {
  const [content, setContent] = React.useState(value.slice(0, limit));

  const setFormattedContent = React.useCallback(
    (text) => {
      setContent(text.slice(0, limit));
    },
    [limit]
  );

  return (
    <>
      <textarea
        rows={rows}
        cols={cols}
        onChange={(event) => setFormattedContent(event.target.value)}
        value={content}
      />
      <p>
        {content.length}/{limit}
      </p>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <LimitedTextarea limit={32} value="Hello!" />
);
```

In diesem Code haben wir:

- Die Kommentare vereinfacht, um einen präziseren Überblick über die Funktion jedes Teils des Codes zu geben.
- Unnötige Codekommentare entfernt.
- Die `setContent`-Funktion aus dem `useCallback`-Abhängigkeitsarray entfernt, da sie nicht erforderlich ist.
- Klammern um das `text`-Argument in der `useCallback`-Funktion hinzugefügt, um die Konsistenz zu gewährleisten.
- Arrow-Funktionen für den `onChange`-Ereignishandler verwendet, um die Kürze zu erhöhen.

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
