# Zusammenziehbarer Inhalt

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Diese Funktion rendert eine zusammenziehbare Komponente mit einem Button, der die Sichtbarkeit ihres Inhalts umschaltet. Hier ist, wie Sie sie verwenden können:

1. Verwenden Sie den `useState()`-Hook, um die `isCollapsed`-Zustandsvariable zu erstellen, die angibt, ob der Inhalt derzeit zusammengelegt oder erweitert ist. Initialisieren Sie es mit `collapsed`.
2. Verwenden Sie das `<button>`-Element, um den `isCollapsed`-Zustand umzuschalten und den über die `children`-Eigenschaft weitergegebenen Inhalt anzuzeigen/auszublenden.
3. Verwenden Sie `isCollapsed`, um der Inhaltscontainer die passende CSS-Klasse `collapsed` oder `expanded` anzuwenden, die seine Erscheinung bestimmt.
4. Aktualisieren Sie das `aria-expanded`-Attribut des Inhaltscontainers basierend auf dem `isCollapsed`-Zustand, um die Komponente für behinderte Benutzer zugänglich zu machen.

Hier ist der für diese Komponente erforderliche CSS-Code:

```css
.collapse-button {
  display: block;
  width: 100%;
}

.collapse-content.collapsed {
  display: none;
}

.collapse-content.expanded {
  display: block;
}
```

Und hier ist der JavaScript-Code:

```jsx
const Collapse = ({ collapsed, children }) => {
  const [isCollapsed, setIsCollapsed] = React.useState(collapsed);

  return (
    <>
      <button
        className="collapse-button"
        onClick={() => setIsCollapsed(!isCollapsed)}
      >
        {isCollapsed ? "Anzeigen" : "Verbergen"} Inhalt
      </button>
      <div
        className={`collapse-content ${isCollapsed ? "collapsed" : "expanded"}`}
        aria-expanded={isCollapsed}
      >
        {children}
      </div>
    </>
  );
};
```

Um diese Komponente zu verwenden, rufen Sie sie einfach mit dem Inhalt auf, den Sie zusammenfalten möchten:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Collapse>
    <h1>Dies ist eine Zusammenfassung</h1>
    <p>Hallo Welt!</p>
  </Collapse>
);
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
