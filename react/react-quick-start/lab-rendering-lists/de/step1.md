# Rendern von Listen

> Das React-Projekt wurde bereits in der virtuellen Maschine (VM) bereitgestellt. Im Allgemeinen müssen Sie nur Code in die Datei `App.js` hinzufügen.

Bitte verwenden Sie den folgenden Befehl, um die Abhängigkeiten zu installieren:

```bash
npm i
```

Sie werden sich auf JavaScript-Funktionen wie die `for`-Schleife und die `map()`-Funktion von Arrays verlassen, um Listen von Komponenten zu rendern.

Beispielsweise haben Sie ein Array von Produkten:

```js
const products = [
  { title: "Cabbage", id: 1 },
  { title: "Garlic", id: 2 },
  { title: "Apple", id: 3 }
];
```

Innerhalb Ihrer Komponente verwenden Sie die `map()`-Funktion, um ein Array von Produkten in ein Array von `<li>`-Elementen umzuwandeln:

```js
const listItems = products.map((product) => (
  <li key={product.id}>{product.title}</li>
));

return <ul>{listItems}</ul>;
```

Beachten Sie, dass `<li>` ein `key`-Attribut hat. Für jedes Element in einer Liste sollten Sie eine Zeichenkette oder eine Zahl übergeben, die dieses Element eindeutig unter seinen Geschwisterelementen identifiziert. Normalerweise sollte der `key` aus Ihren Daten stammen, wie z. B. einer Datenbank-ID. React verwendet Ihre `key`s, um zu verstehen, was passiert, wenn Sie später Elemente einfügen, löschen oder neu anordnen.

```js
// App.js
const products = [
  { title: "Cabbage", isFruit: false, id: 1 },
  { title: "Garlic", isFruit: false, id: 2 },
  { title: "Apple", isFruit: true, id: 3 }
];

export default function ShoppingList() {
  const listItems = products.map((product) => (
    <li
      key={product.id}
      style={{
        color: product.isFruit ? "magenta" : "darkgreen"
      }}
    >
      {product.title}
    </li>
  ));

  return <ul>{listItems}</ul>;
}
```

Um das Projekt auszuführen, verwenden Sie den folgenden Befehl. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzusehen.

```bash
npm start
```
