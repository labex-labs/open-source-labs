# Unkontrolliertes Eingabefeld

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Dieser Code rendert ein unkontrolliertes `<input>`-Element, das eine Callback-Funktion verwendet, um seine übergeordnete Komponente über Wertesaktualisierungen zu informieren. Um es zu verwenden:

- Übergeben Sie den Anfangswert von der übergeordneten Komponente mithilfe der `defaultValue`-Eigenschaft.
- Übergeben Sie eine Callback-Funktion namens `onValueChange`, um Wertesaktualisierungen zu behandeln.
- Verwenden Sie das `onChange`-Ereignis, um die Callback-Funktion auszulösen und den neuen Wert an die übergeordnete Komponente zu senden.

Hier ist ein Beispiel:

```jsx
const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
  return (
    <input
      defaultValue={defaultValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <UncontrolledInput
    type="text"
    placeholder="Fügen Sie hier etwas Text ein..."
    onValueChange={console.log}
  />
);
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
