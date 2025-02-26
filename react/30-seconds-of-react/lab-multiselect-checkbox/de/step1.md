# Zustandsbehaftete Checkbox mit Mehrfachauswahl

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Dieser Code rendert eine Liste von Checkboxen und sendet den/die ausgewählten Wert(e) an die übergeordnete Komponente mithilfe einer Callback-Funktion. Hier sind die Schritte, um es zu erstellen:

1. Verwenden Sie den `useState()`-Hook, um die `data`-Zustandsvariable mit der `options`-Eigenschaft zu initialisieren.
2. Erstellen Sie eine `toggle`-Funktion, die die `data`-Zustandsvariable mit der/den ausgewählten Option(en) aktualisiert und die `onChange`-Callback-Funktion mit ihnen aufruft.
3. Mappen Sie die `data`-Zustandsvariable, um individuelle Checkboxen und ihre Labels zu generieren. Binden Sie die `toggle`-Funktion an den `onClick`-Handler jeder Checkbox.

```jsx
const MultiselectCheckbox = ({ options, onChange }) => {
  const [data, setData] = React.useState(options);

  const toggle = (index) => {
    const newData = [...data];
    newData[index] = {
      ...newData[index],
      checked: !newData[index].checked
    };
    setData(newData);
    onChange(newData.filter((item) => item.checked));
  };

  return (
    <>
      {data.map((item, index) => (
        <label key={item.label}>
          <input
            type="checkbox"
            checked={item.checked || false}
            onChange={() => toggle(index)}
          />
          {item.label}
        </label>
      ))}
    </>
  );
};
```

Hier ist ein Beispiel, wie es verwendet werden kann:

```jsx
const options = [{ label: "Item One" }, { label: "Item Two" }];

ReactDOM.createRoot(document.getElementById("root")).render(
  <MultiselectCheckbox
    options={options}
    onChange={(selected) => {
      console.log(selected);
    }}
  />
);
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
