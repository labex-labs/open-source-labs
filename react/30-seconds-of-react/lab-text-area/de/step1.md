# Unkontrolliertes Textarea-Element

> `index.html` und `script.js` wurden bereits in der VM bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Diese Funktion rendert ein `<textarea>`-Element, das nicht von der übergeordneten Komponente kontrolliert wird. Sie verwendet eine Callback-Funktion, um den Wert der Eingabe an die übergeordnete Komponente zu übergeben.

Um diese Funktion zu verwenden:

- Übergeben Sie die `defaultValue`-Eigenschaft von der übergeordneten Komponente als Initialwert des Eingabefelds.
- Verwenden Sie das `onChange`-Ereignis, um den `onValueChange`-Callback auszulösen und den neuen Wert an die übergeordnete Komponente zu senden.

```jsx
const TextArea = ({
  cols = 20,
  rows = 2,
  defaultValue,
  onValueChange,
  ...rest
}) => {
  return (
    <textarea
      cols={cols}
      rows={rows}
      defaultValue={defaultValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};
```

Beispielverwendung:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <TextArea
    placeholder="Fügen Sie hier etwas Text ein..."
    onValueChange={(val) => console.log(val)}
  />
);
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
