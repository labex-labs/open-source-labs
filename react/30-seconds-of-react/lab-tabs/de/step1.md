# Tabs

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Um ein Tab-Menü und eine Ansichts-Komponente zu rendern, folgen Sie diesen Schritten:

1. Definieren Sie eine `Tabs`-Komponente. Verwenden Sie den `useState()`-Hook, um die `bindIndex`-Zustandsvariable auf `defaultIndex` zu setzen.
2. Definieren Sie eine `TabItem`-Komponente und filtern Sie die `children`, die an die `Tabs`-Komponente übergeben werden, um alle unnötigen Knoten außer `TabItem` zu entfernen. Sie können dies tun, indem Sie den Funktionsnamen identifizieren.
3. Definieren Sie eine Funktion namens `changeTab`. Diese Funktion wird ausgeführt, wenn ein Benutzer auf einen `<button>` im Menü klickt.
4. `changeTab` führt den übergebenen Callback `onTabClick` aus und aktualisiert `bindIndex` basierend auf dem angeklickten Element.
5. Verwenden Sie `Array.prototype.map()` auf den gesammelten Knoten, um das Menü und die Ansicht der Tabs zu rendern.
6. Verwenden Sie den Wert von `bindIndex`, um den aktiven Tab zu bestimmen und die richtige `className` anzuwenden.

Hier ist der CSS-Code, um das Tab-Menü und die Ansicht zu gestalten:

```css
.tab-menu > button {
  cursor: pointer;
  padding: 8px 16px;
  border: 0;
  border-bottom: 2px solid transparent;
  background: none;
}

.tab-menu > button.focus {
  border-bottom: 2px solid #007bef;
}

.tab-menu > button:hover {
  border-bottom: 2px solid #007bef;
}

.tab-content {
  display: none;
}

.tab-content.selected {
  display: block;
}
```

Hier ist der JavaScript-Code, um die `Tabs`-Komponente zu implementieren:

```jsx
const TabItem = (props) => <div {...props} />;

const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
  const [bindIndex, setBindIndex] = React.useState(defaultIndex);

  const changeTab = (newIndex) => {
    if (typeof onTabClick === "function") onTabClick(newIndex);
    setBindIndex(newIndex);
  };

  const items = children.filter((item) => item.type.name === "TabItem");

  return (
    <div className="wrapper">
      <div className="tab-menu">
        {items.map(({ props: { index, label } }) => (
          <button
            key={`tab-btn-${index}`}
            onClick={() => changeTab(index)}
            className={bindIndex === index ? "focus" : ""}
          >
            {label}
          </button>
        ))}
      </div>
      <div className="tab-view">
        {items.map(({ props }) => (
          <div
            {...props}
            className={`tab-content ${
              bindIndex === props.index ? "selected" : ""
            }`}
            key={`tab-content-${props.index}`}
          />
        ))}
      </div>
    </div>
  );
};
```

Schließlich ist hier ein Beispiel, wie die `Tabs`-Komponente verwendet wird:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Tabs defaultIndex={1} onTabClick={console.log}>
    <TabItem label="A" index={1}>
      Lorem ipsum
    </TabItem>
    <TabItem label="B" index={2}>
      Dolor sit amet
    </TabItem>
  </Tabs>
);
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite zu previewen.
