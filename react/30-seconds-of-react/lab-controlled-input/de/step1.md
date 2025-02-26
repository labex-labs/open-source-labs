# Kontrolliertes Eingabefeld

> `index.html` und `script.js` wurden bereits in der VM bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Dieser Codeausschnitt stellt ein kontrolliertes `<input>`-Element bereit, das eine Callback-Funktion verwendet, um seine übergeordnete Komponente über alle Updates seines Werts zu informieren. So funktioniert es:

- Der Wert des kontrollierten Eingabefelds wird durch die `value`-Eigenschaft bestimmt, die von der übergeordneten Komponente weitergegeben wird.
- Alle Änderungen, die der Benutzer am Eingabefeld vornimmt, werden durch das `onChange`-Ereignis erfasst, das die `onValueChange`-Callback-Funktion auslöst und den neuen Wert an die übergeordnete Komponente zurücksendet.
- Um den Wert des Eingabefelds zu aktualisieren, muss die übergeordnete Komponente die `value`-Eigenschaft aktualisieren, die sie an das kontrollierte Eingabekomponente weitergibt.

Hier ist ein Beispielimplementierung der `ControlledInput`-Komponente, gefolgt von einem Verwendungsexempel in einer `Form`-Komponente:

```jsx
const ControlledInput = ({ value, onValueChange, ...rest }) => {
  return (
    <input
      value={value}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};

const Form = () => {
  const [value, setValue] = React.useState("");

  return (
    <ControlledInput
      type="text"
      placeholder="Fügen Sie hier etwas Text ein..."
      value={value}
      onValueChange={setValue}
    />
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Form />);
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
