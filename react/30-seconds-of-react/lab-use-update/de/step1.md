# React useUpdate-Hook

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Um einen Komponenten dazu zu zwingen, sich bei einem Aufruf neu zu rendern, verwenden Sie den `useReducer()`-Hook, um jedes Mal, wenn er aktualisiert wird, ein neues Objekt zu erstellen und seine `dispatch` zurückzugeben. Hier ist eine Beispielimplementierung der `useUpdate()`-Funktion:

```jsx
const useUpdate = () => {
  const [, update] = React.useReducer(() => ({}));
  return update;
};
```

Sie können dann `useUpdate()` in Ihrem Komponenten verwenden, um eine Neuerstellung zu verursachen, wenn dies erforderlich ist:

```jsx
const MyApp = () => {
  const update = useUpdate();

  return (
    <>
      <div>Zeit: {Date.now()}</div>
      <button onClick={update}>Aktualisieren</button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
