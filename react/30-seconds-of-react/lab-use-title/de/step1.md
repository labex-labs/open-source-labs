# React useTitle-Hook

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Um den Titel der Seite zu setzen, können Sie den benutzerdefinierten `useTitle`-Hook verwenden. Dieser Hook verwendet `typeof`, um zu überprüfen, ob `Document` definiert ist. Wenn dies der Fall ist, wird der `useRef()`-Hook verwendet, um den ursprünglichen Titel des `Document` zu speichern. Anschließend wird der `useEffect()`-Hook verwendet, um `Document.title` auf den übergebenen Wert beim Mounten der Komponente festzulegen und beim Entfernen aufzuräumen.

```jsx
const useTitle = (title) => {
  const documentDefined = typeof document !== "undefined";
  const originalTitle = React.useRef(documentDefined ? document.title : null);

  React.useEffect(() => {
    if (!documentDefined) return;

    if (document.title !== title) {
      document.title = title;
    }

    return () => {
      document.title = originalTitle.current;
    };
  }, [title]);
};
```

Im Beispielcode verwendet die `Alert`-Komponente den `useTitle`-Hook, um den Titel auf "Alert" zu setzen. Die `MyApp`-Komponente rendert einen Button, der die `Alert`-Komponente umschaltet.

```jsx
const Alert = () => {
  useTitle("Alert");

  return (
    <div>
      <p>Alert! Title has changed</p>
    </div>
  );
};

const MyApp = () => {
  const [alertOpen, setAlertOpen] = React.useState(false);

  return (
    <div>
      <button onClick={() => setAlertOpen(!alertOpen)}>Toggle alert</button>
      {alertOpen && <Alert />}
    </div>
  );
};

ReactDOM.render(<MyApp />, document.getElementById("root"));
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
