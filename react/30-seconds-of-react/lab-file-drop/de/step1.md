# Datei-Ziehen-und-Zwischenlegen-Bereich

> `index.html` und `script.js` wurden bereits in der VM bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Diese Komponente ermöglicht das Ziehen und Zwischenlegen von einer einzelnen Datei. Um diese Komponente zu implementieren, folgen Sie diesen Schritten:

1. Erstellen Sie einen Verweis namens `dropRef` und binden Sie ihn an die Umhüllung der Komponente.
2. Verwenden Sie den `useState()`-Hook, um die Variablen `drag` und `filename` zu erstellen. Initialisieren Sie sie mit `false` bzw. `''`.
3. Die Variablen `dragCounter` und `drag` werden verwendet, um zu bestimmen, ob eine Datei gezogen wird, während `filename` verwendet wird, um den Namen der abgelegten Datei zu speichern.
4. Erstellen Sie die Methoden `handleDrag`, `handleDragIn`, `handleDragOut` und `handleDrop`, um die Ziehen-und-Zwischenlegen-Funktionalität zu behandeln. `handleDrag` verhindert, dass der Browser die gezogene Datei öffnet, `handleDragIn` und `handleDragOut` behandeln das Betreten und Verlassen der Komponente durch die gezogene Datei, und `handleDrop` behandelt das Ablegen der Datei und übergibt sie an `onDrop`.
5. Verwenden Sie den `useEffect()`-Hook, um jedes der Ziehen-und-Zwischenlegen-Ereignisse mit den zuvor erstellten Methoden zu behandeln.

Hier ist die CSS für die Komponente:

```css
.filedrop {
  min-height: 120px;
  border: 3px solid #d3d3d3;
  text-align: center;
  font-size: 24px;
  padding: 32px;
  border-radius: 4px;
}

.filedrop.drag {
  border: 3px durchgezogener Strich #1e90ff;
}

.filedrop.ready {
  border: 3px solid #32cd32;
}
```

Hier ist der JSX für die Komponente:

```jsx
const FileDrop = ({ onDrop }) => {
  const [drag, setDrag] = React.useState(false);
  const [filename, setFilename] = React.useState("");
  const dropRef = React.useRef(null);
  let dragCounter = 0;

  const handleDrag = (e) => {
    e.preventDefault();
    e.stopPropagation();
  };

  const handleDragIn = (e) => {
    e.preventDefault();
    e.stopPropagation();
    dragCounter++;
    if (e.dataTransfer.items && e.dataTransfer.items.length > 0) setDrag(true);
  };

  const handleDragOut = (e) => {
    e.preventDefault();
    e.stopPropagation();
    dragCounter--;
    if (dragCounter === 0) setDrag(false);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setDrag(false);
    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
      onDrop(e.dataTransfer.files[0]);
      setFilename(e.dataTransfer.files[0].name);
      e.dataTransfer.clearData();
      dragCounter = 0;
    }
  };

  React.useEffect(() => {
    const div = dropRef.current;
    div.addEventListener("dragenter", handleDragIn);
    div.addEventListener("dragleave", handleDragOut);
    div.addEventListener("dragover", handleDrag);
    div.addEventListener("drop", handleDrop);
    return () => {
      div.removeEventListener("dragenter", handleDragIn);
      div.removeEventListener("dragleave", handleDragOut);
      div.removeEventListener("dragover", handleDrag);
      div.removeEventListener("drop", handleDrop);
    };
  }, []);

  return (
    <div
      ref={dropRef}
      className={
        drag ? "filedrop drag" : filename ? "filedrop ready" : "filedrop"
      }
    >
      {filename && !drag ? (
        <div>{filename}</div>
      ) : (
        <div>Ziehen Sie eine Datei hierher!</div>
      )}
    </div>
  );
};
```

Um die Komponente zu verwenden, rufen Sie `ReactDOM.createRoot(document.getElementById('root')).render(<FileDrop onDrop={console.log} />);` auf.

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
