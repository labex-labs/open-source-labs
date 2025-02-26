# Erweiterbare Objektbaumansicht

> `index.html` und `script.js` wurden bereits in der VM bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Der folgende Code rendert eine zusammenziehbare Baumansicht eines JSON-Objekts oder -Arrays. Indem Sie den `useState()`-Hook verwenden, um die `isToggled`-Zustandsvariable zu erstellen, können Sie den Anfangszustand des Inhalts (zusammengeklappt/erweitert) durch Übergeben der `toggled`-Eigenschaft bestimmen. Die Erscheinung der Komponente wird basierend auf `isParentToggled`, `isToggled`, `name` und der Prüfung auf `Array.isArray()` für `data` bestimmt.

Für jedes Kind in `data` bestimmen Sie, ob es ein Objekt oder ein Array ist, und rendern Sie rekursiv einen Unterbaum oder ein Textelement mit dem entsprechenden Stil. Um den Komponentenstatus umzuschalten, rendern Sie ein `<span>`-Element und binden Sie sein `onClick`-Ereignis, um den `isToggled`-Zustand der Komponente zu ändern.

Die CSS-Stile werden für die Erscheinung der Komponente definiert, einschließlich der `margin`, `position`, `border`- und `display`-Eigenschaften.

```jsx
const TreeView = ({
  data,
  toggled = true,
  name = null,
  isLast = true,
  isChildElement = false,
  isParentToggled = true
}) => {
  const [isToggled, setIsToggled] = React.useState(toggled);
  const isDataArray = Array.isArray(data);

  return (
    <div
      className={`tree-element ${isParentToggled && "collapsed"} ${
        isChildElement && "is-child"
      }`}
    >
      <span
        className={isToggled ? "toggler" : "toggler closed"}
        onClick={() => setIsToggled(!isToggled)}
      />
      {name ? <strong>&nbsp;&nbsp;{name}: </strong> : <span>&nbsp;&nbsp;</span>}
      {isDataArray ? "[" : "{"}
      {!isToggled && "..."}
      {Object.keys(data).map((v, i, a) =>
        typeof data[v] === "object" ? (
          <TreeView
            key={`${name}-${v}-${i}`}
            data={data[v]}
            isLast={i === a.length - 1}
            name={isDataArray ? null : v}
            isChildElement
            isParentToggled={isParentToggled && isToggled}
          />
        ) : (
          <p
            key={`${name}-${v}-${i}`}
            className={isToggled ? "tree-element" : "tree-element collapsed"}
          >
            {isDataArray ? "" : <strong>{v}: </strong>}
            {data[v]}
            {i === a.length - 1 ? "" : ","}
          </p>
        )
      )}
      {isDataArray ? "]" : "}"}
      {!isLast ? "," : ""}
    </div>
  );
};
```

```css
.tree-element {
  margin: 0 0 0 4px;
  position: relative;
}

.tree-element.is-child {
  margin-left: 16px;
}

div.tree-element::before {
  content: "";
  position: absolute;
  top: 24px;
  left: 1px;
  height: calc(100% - 48px);
  border-left: 1px solid gray;
}

p.tree-element {
  margin-left: 16px;
}

.toggler {
  position: absolute;
  top: 10px;
  left: 0px;
  width: 0;
  height: 0;
  border-top: 4px solid transparent;
  border-bottom: 4px solid transparent;
  border-left: 5px solid gray;
  cursor: pointer;
}

.toggler.closed {
  transform: rotate(90deg);
}

.collapsed {
  display: none;
}
```

```jsx
const data = {
  lorem: {
    ipsum: "dolor sit",
    amet: {
      consectetur: "adipiscing",
      elit: [
        "duis",
        "vitae",
        {
          semper: "orci"
        },
        {
          est: "sed ornare"
        },
        "etiam",
        ["laoreet", "tincidunt"],
        ["vestibulum", "ante"]
      ]
    },
    ipsum: "primis"
  }
};
ReactDOM.createRoot(document.getElementById("root")).render(
  <TreeView data={data} name="data" />
);
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite zu previewen.
