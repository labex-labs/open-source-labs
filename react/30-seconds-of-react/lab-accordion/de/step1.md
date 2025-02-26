# Zusammenziehbares Akkordeon

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Um ein Akkordeon-Menü mit mehreren zusammenziehbaren Inhaltelementen zu rendern, können Sie die folgenden Schritte ausführen:

1. Definieren Sie einen `AccordionItem`-Komponenten, der einen `<button>` rendert und die Komponente aktualisiert, während es über den `handleClick`-Callback seinen Elternteil benachrichtigt.
2. Verwenden Sie die `isCollapsed`-Eigenschaft in `AccordionItem`, um dessen Erscheinung zu bestimmen und seine `className` festzulegen.
3. Definieren Sie eine `Accordion`-Komponente und verwenden Sie den `useState()`-Hook, um den Wert der `bindIndex`-Zustandsvariable auf `defaultIndex` zu initialisieren.
4. Filtern Sie `children`, um unnötige Knoten zu entfernen, außer `AccordionItem`, indem Sie den Namen der Funktion identifizieren.
5. Verwenden Sie `Array.prototype.map()` auf den gesammelten Knoten, um die einzelnen zusammenziehbaren Elemente zu rendern.
6. Definieren Sie `changeItem`, die ausgeführt wird, wenn auf den `<button>` eines `AccordionItem` geklickt wird.
7. `changeItem` führt den übergebenen Callback `onItemClick` aus und aktualisiert `bindIndex` basierend auf dem geklickten Element.

Hier ist der Code:

```css
.accordion-item.collapsed {
  display: none;
}

.accordion-item.expanded {
  display: block;
}

.accordion-button {
  display: block;
  width: 100%;
}
```

```jsx
const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
  return (
    <>
      <button className="accordion-button" onClick={handleClick}>
        {label}
      </button>
      <div
        className={`accordion-item ${isCollapsed ? "collapsed" : "expanded"}`}
        aria-expanded={isCollapsed}
      >
        {children}
      </div>
    </>
  );
};

const Accordion = ({ defaultIndex, onItemClick, children }) => {
  const [bindIndex, setBindIndex] = React.useState(defaultIndex);

  const changeItem = (itemIndex) => {
    if (typeof onItemClick === "function") onItemClick(itemIndex);
    if (itemIndex !== bindIndex) setBindIndex(itemIndex);
  };

  const items = children.filter((item) => item.type.name === "AccordionItem");

  return (
    <>
      {items.map(({ props }) => (
        <AccordionItem
          isCollapsed={bindIndex !== props.index}
          label={props.label}
          handleClick={() => changeItem(props.index)}
          children={props.children}
        />
      ))}
    </>
  );
};
```

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Accordion defaultIndex="1" onItemClick={console.log}>
    <AccordionItem label="A" index="1">
      Lorem ipsum
    </AccordionItem>
    <AccordionItem label="B" index="2">
      Dolor sit amet
    </AccordionItem>
  </Accordion>
);
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite zu previewen.
