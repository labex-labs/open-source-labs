# Daten Tabelle

> `index.html` und `script.js` wurden bereits in der VM bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Erstellen Sie ein Tabellenelement mit zwei Spalten, `ID` und `Value`, wobei jede Zeile aus einem Array von primitiven Werten dynamisch generiert wird.

Um dies zu erreichen, verwenden Sie die `Array.prototype.map()`-Methode, um ein neues Array von JSX-Elementen zu erstellen, die jedes Element im Eingabe-`data`-Array als `<tr>`-Element mit einem geeigneten `key` darstellen. Innerhalb jedes `<tr>` fügen Sie zwei `<td>`-Elemente hinzu, um die Zeilennummer und den Wert der Zeile jeweils anzuzeigen.

Hier ist eine Beispielimplementierung:

```jsx
const DataTable = ({ data }) => {
  return (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Value</th>
        </tr>
      </thead>
      <tbody>
        {data.map((val, i) => (
          <tr key={`${i}_${val}`}>
            <td>{i}</td>
            <td>{val}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};
```

Um dieses Komponenten mit einem Array von Vornamen zu verwenden, können Sie es beispielsweise wie folgt aufrufen:

```jsx
const people = ["John", "Jesse"];
ReactDOM.createRoot(document.getElementById("root")).render(
  <DataTable data={people} />
);
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
