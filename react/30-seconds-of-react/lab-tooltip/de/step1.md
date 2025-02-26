# Tooltip

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Hier ist eine klarere, präzisere und kohärentere Version des Inhalts:

---

Dieser Code erstellt eine Tooltip-Komponente. Um sie zu verwenden, tun Sie Folgendes:

1. Verwenden Sie den `useState()`-Hook, um die Variable `show` zu erstellen und auf `false` zu setzen.
2. Rendern Sie ein Container-Element, das das Tooltip-Element und die an die Komponente übergebenen `children` enthält.
3. Behandeln Sie die `onMouseEnter`- und `onMouseLeave`-Ereignisse, indem Sie die `className` des Tooltips umschalten, die von der `show`-Variable gesteuert wird.

Hier ist der Code für die Tooltip-Komponente:

```css
.tooltip-container {
  position: relative;
}

.tooltip-box {
  position: absolute;
  top: calc(100% + 5px);
  display: none;
  padding: 5px;
  border-radius: 5px;
  background: rgba(0, 0, 0, 0.7);
  color: #fff;
}

.tooltip-box.visible {
  display: block;
}

.tooltip-arrow {
  position: absolute;
  top: -10px;
  left: 50%;
  border-width: 5px;
  border-style: solid;
  border-color: transparent transparent rgba(0, 0, 0, 0.7) transparent;
}
```

```jsx
const Tooltip = ({ children, text, ...rest }) => {
  const [show, setShow] = React.useState(false);

  return (
    <div className="tooltip-container">
      <div className={show ? "tooltip-box visible" : "tooltip-box"}>
        {text}
        <span className="tooltip-arrow" />
      </div>
      <div
        onMouseEnter={() => setShow(true)}
        onMouseLeave={() => setShow(false)}
        {...rest}
      >
        {children}
      </div>
    </div>
  );
};
```

Um die Tooltip-Komponente zu verwenden, rufen Sie `ReactDOM.createRoot()` mit dem folgenden Code auf:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Tooltip text="Simple tooltip">
    <button>Hover me!</button>
  </Tooltip>
);
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
