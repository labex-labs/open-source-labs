# React useClickInside-Hook

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Um ein Klickereignis innerhalb einer Komponente zu behandeln, können Sie einen benutzerdefinierten Hook namens `useClickInside` erstellen, der eine `ref` und einen `callback` entgegennimmt. Verwenden Sie den Hook `useEffect()`, um das `click`-Ereignis hinzuzufügen und aufzuräumen, und den Hook `useRef()`, um eine `ref` für Ihre Klickkomponente zu erstellen und an den Hook `useClickInside` zu übergeben. Hier ist der Code:

```jsx
const useClickInside = (ref, callback) => {
  const handleClick = (e) => {
    if (ref.current && ref.current.contains(e.target)) {
      callback();
    }
  };

  React.useEffect(() => {
    document.addEventListener("click", handleClick);
    return () => {
      document.removeEventListener("click", handleClick);
    };
  }, [ref, callback]);
};
```

Sie können diesen Hook in Ihrer Komponente wie folgt verwenden:

```jsx
const ClickBox = ({ onClickInside }) => {
  const clickRef = React.useRef();
  useClickInside(clickRef, onClickInside);

  return (
    <div
      className="click-box"
      ref={clickRef}
      style={{
        border: "2px durchgezogener orangefarbenes Rot",
        Höhe: 200,
        Breite: 400,
        display: "flex",
        justifyContent: "center",
        alignItems: "center"
      }}
    >
      <p>Klicken Sie innerhalb dieses Elements</p>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <ClickBox onClickInside={() => alert("innerhalb klicken")} />
);
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
