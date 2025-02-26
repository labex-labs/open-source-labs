# React useClickOutside-Hook

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Dieser Code behandelt das Ereignis, außerhalb eines umfassten Komponenten zu klicken. Er funktioniert, indem ein benutzerdefinierter Hook erstellt wird, der eine `ref` und einen `callback` für das Behandeln des `click`-Ereignisses übernimmt. Der `useEffect()`-Hook wird verwendet, um das `click`-Ereignis hinzuzufügen und aufzuräumen, während der `useRef()`-Hook verwendet wird, um eine `ref` für die Klickkomponente zu erstellen und an den `useClickOutside`-Hook zu übergeben.

```jsx
const useClickOutside = (ref, callback) => {
  const handleClick = (e) => {
    if (ref.current && !ref.current.contains(e.target)) {
      callback();
    }
  };
  React.useEffect(() => {
    document.addEventListener("click", handleClick);
    return () => {
      document.removeEventListener("click", handleClick);
    };
  });
};

const ClickBox = ({ onClickOutside }) => {
  const clickRef = React.useRef();
  useClickOutside(clickRef, onClickOutside);
  return (
    <div
      className="click-box"
      ref={clickRef}
      style={{
        border: "2px durchgezogener orangefarben",
        Höhe: 200,
        Breite: 400,
        display: "flex",
        justifyContent: "center",
        alignItems: "center"
      }}
    >
      <p>Klicken Sie außerhalb dieses Elements</p>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <ClickBox onClickOutside={() => alert("außerhalb klicken")} />
);
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
