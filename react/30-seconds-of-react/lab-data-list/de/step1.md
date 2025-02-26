# Datenliste

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Diese Funktion rendert eine Liste von Elementen aus einem Array von primitiven Werten. Sie kann verwendet werden, um eine nummerierte oder aufzählungsfreie Liste bedingt basierend auf dem Wert der `isOrdered`-Eigenschaft zu rendern. Um jedes Element aus dem `data`-Array zu rendern, verwendet sie `Array.prototype.map()`, um ein `<li>`-Element mit einem eindeutigen `key` für jedes Element zu erstellen.

```jsx
const DataList = ({ data, isOrdered = false }) => {
  const list = data.map((value, index) => (
    <li key={`${index}_${value}`}>{value}</li>
  ));

  return isOrdered ? <ol>{list}</ol> : <ul>{list}</ul>;
};
```

Hier ist ein Beispiel dafür, wie Sie diese Komponente verwenden können:

```jsx
const names = ["John", "Paul", "Mary"];
ReactDOM.createRoot(document.getElementById("root")).render(
  <>
    <DataList data={names} />
    <DataList data={names} isOrdered={true} />
  </>
);
```

In diesem Beispiel übergeben wir ein Array von Namen an die `DataList`-Komponente und rendern es两次. Zum ersten Mal rendern wir eine aufzählungsfreie Liste, während wir zum zweiten Mal eine nummerierte Liste rendern.

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
