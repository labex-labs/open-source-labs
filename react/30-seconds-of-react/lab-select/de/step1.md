# Unkontrolliertes Select-Element

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Dies ist ein Element, das ein kontrolliertes `<select>`-Element rendert. Das Element akzeptiert ein Array von Werten und eine Callback-Funktion, um den ausgewählten Wert an sein übergeordnetes Element zu übergeben. Hier sind die Schritte, um dieses Element zu verwenden:

- Verwenden Sie die `selectedValue`-Eigenschaft, um den Anfangswert des `<select>`-Elements festzulegen.
- Verwenden Sie die `onValueChange`-Eigenschaft, um die Callback-Funktion anzugeben, die aufgerufen werden soll, wenn der Wert des `<select>`-Elements geändert wird.
- Verwenden Sie `Array.prototype.map()` auf dem `values`-Array, um für jeden übergebenen Wert ein `<option>`-Element zu erstellen.
- Jeder Eintrag in `values` sollte ein zweielementiges Array sein, wobei das erste Element der `value` des Elements und das zweite das angezeigte Textfeld ist.

```jsx
const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
  return (
    <select
      defaultValue={selectedValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    >
      {values.map(([value, text]) => (
        <option key={value} value={value}>
          {text}
        </option>
      ))}
    </select>
  );
};
```

Hier ist ein Beispiel, wie dieses Element verwendet werden kann:

```jsx
const choices = [
  ["grapefruit", "Grapefruit"],
  ["lime", "Lime"],
  ["coconut", "Coconut"],
  ["mango", "Mango"]
];

ReactDOM.createRoot(document.getElementById("root")).render(
  <Select
    values={choices}
    selectedValue="lime"
    onValueChange={(val) => console.log(val)}
  />
);
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
