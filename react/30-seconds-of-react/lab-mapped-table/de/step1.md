# Objekt-Tabellenansicht

> `index.html` und `script.js` wurden bereits in der VM bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Diese Komponente rendert eine Tabelle mit Zeilen, die dynamisch aus einem Array von Objekten und einer Liste von Eigenschaftennamen erstellt werden. Um dies zu erreichen:

- Verwenden Sie `Object.keys()`, `Array.prototype.filter()`, `Array.prototype.includes()` und `Array.prototype.reduce()`, um ein `filteredData`-Array zu erzeugen, das alle Objekte enthält, deren Schlüssel in `propertyNames` angegeben sind.
- Rendern Sie ein `<table>`-Element mit einer Anzahl von Spalten, die der Anzahl der Werte in `propertyNames` entspricht.
- Verwenden Sie `Array.prototype.map()`, um jeden Wert im `propertyNames`-Array als `<th>`-Element zu rendern.
- Verwenden Sie `Array.prototype.map()`, um jedes Objekt im `filteredData`-Array als `<tr>`-Element zu rendern, das für jeden Schlüssel im Objekt ein `<td>` enthält.
- Beachten Sie, dass diese Komponente nicht mit geschachtelten Objekten funktioniert und abbrechen wird, wenn in einem der in `propertyNames` angegebenen Eigenschaften geschachtelte Objekte vorhanden sind.

Hier ist der Code:

```jsx
const MappedTable = ({ data, propertyNames }) => {
  const filteredData = data.map((obj) =>
    Object.keys(obj)
      .filter((key) => propertyNames.includes(key))
      .reduce((acc, key) => ({ ...acc, [key]: obj[key] }), {})
  );

  return (
    <table>
      <thead>
        <tr>
          {propertyNames.map((name) => (
            <th key={`header-${name}`}>{name}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {filteredData.map((obj, i) => (
          <tr key={`row-${i}`}>
            {propertyNames.map((name) => (
              <td key={`cell-${i}-${name}`}>{obj[name]}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
};
```

Sie können die Komponente verwenden, indem Sie ein Array von Objekten und eine Liste von Eigenschaftennamen übergeben:

```jsx
const people = [
  { name: "John", surname: "Smith", age: 42 },
  { name: "Adam", surname: "Smith", gender: "male" }
];
const propertyNames = ["name", "surname", "age"];

ReactDOM.render(
  <MappedTable data={people} propertyNames={propertyNames} />,
  document.getElementById("root")
);
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite zu previewen.
