# Unkontrolliertes Range-Eingabefeld

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Um einen Schieberegler in React zu erstellen, verwenden Sie die `Slider`-Komponente und übergeben Sie die `min`, `max`, `defaultValue` und `onValueChange`-Props.

In der `Slider`-Komponente legen Sie den `type` des `<input>`-Elements auf `"range"` fest, um einen Schieberegler zu erstellen. Verwenden Sie die von der übergeordneten Komponente übergebene `defaultValue` als Anfangswert für das unkontrollierte Eingabefeld. Verwenden Sie das `onChange`-Ereignis, um den `onValueChange`-Callback auszulösen und den neuen Wert an die übergeordnete Komponente zu senden.

Hier ist der Code für die `Slider`-Komponente:

```jsx
const Slider = ({
  min = 0,
  max = 100,
  defaultValue,
  onValueChange,
  ...rest
}) => {
  return (
    <input
      type="range"
      min={min}
      max={max}
      defaultValue={defaultValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};
```

Um die `Slider`-Komponente zu rendern, verwenden Sie `ReactDOM.createRoot` und übergeben Sie die `onValueChange`-Callback-Funktion:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Slider onValueChange={(val) => console.log(val)} />
);
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
