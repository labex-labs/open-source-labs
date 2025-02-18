# Button mit Welleneffekt

> `index.html` und `script.js` wurden bereits in der virtuellen Maschine (VM) bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Dieser Code rendert eine Button-Komponente, die beim Klicken einen Welleneffekt erzeugt. So funktioniert es:

- Der `useState()`-Hook wird verwendet, um zwei Zustandsvariablen zu erstellen: `coords` und `isRippling`. Die Variable `coords` speichert die Koordinaten des Zeigers, während `isRippling` den Animationszustand des Buttons speichert.
- Ein `useEffect()`-Hook wird verwendet, um den Wert von `isRippling` jedes Mal zu ändern, wenn sich die Zustandsvariable `coords` ändert. Dies startet die Animation des Welleneffekts.
- `setTimeout()` wird im vorherigen Hook verwendet, um die Animation nach dem Abspielen zu löschen.
- Ein weiterer `useEffect()`-Hook wird verwendet, um `coords` zurückzusetzen, wenn die Zustandsvariable `isRippling` `false` ist.
- Das `onClick`-Ereignis wird behandelt, indem die Zustandsvariable `coords` aktualisiert und die übergebene Callback-Funktion aufgerufen wird.

Hier ist der Code für die `RippleButton`-Komponente:

```jsx
const RippleButton = ({ children, onClick }) => {
  const [coords, setCoords] = React.useState({ x: -1, y: -1 });
  const [isRippling, setIsRippling] = React.useState(false);

  React.useEffect(() => {
    if (coords.x !== -1 && coords.y !== -1) {
      setIsRippling(true);
      setTimeout(() => setIsRippling(false), 300);
    } else setIsRippling(false);
  }, [coords]);

  React.useEffect(() => {
    if (!isRippling) setCoords({ x: -1, y: -1 });
  }, [isRippling]);

  return (
    <button
      className="ripple-button"
      onClick={(e) => {
        const rect = e.target.getBoundingClientRect();
        setCoords({ x: e.clientX - rect.left, y: e.clientY - rect.top });
        onClick && onClick(e);
      }}
    >
      {isRippling && (
        <span
          className="ripple"
          style={{
            left: coords.x,
            top: coords.y
          }}
        />
      )}
      <span className="content">{children}</span>
    </button>
  );
};
```

Sie können diese Komponente wie folgt verwenden:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <RippleButton onClick={(e) => console.log(e)}>Click me</RippleButton>
);
```

Und hier ist der CSS-Code für die `RippleButton`-Komponente:

```css
.ripple-button {
  border-radius: 4px;
  border: none;
  margin: 8px;
  padding: 14px 24px;
  background: #1976d2;
  color: #fff;
  overflow: hidden;
  position: relative;
  cursor: pointer;
}

.ripple-button > .ripple {
  width: 20px;
  height: 20px;
  position: absolute;
  background: #63a4ff;
  display: block;
  content: "";
  border-radius: 9999px;
  opacity: 1;
  animation: 0.9s ease 1 forwards ripple-effect;
}

@keyframes ripple-effect {
  0% {
    transform: scale(1);
    opacity: 1;
  }
  50% {
    transform: scale(10);
    opacity: 0.375;
  }
  100% {
    transform: scale(35);
    opacity: 0;
  }
}

.ripple-button > .content {
  position: relative;
  z-index: 2;
}
```

Klicken Sie bitte auf 'Go Live' in der unteren rechten Ecke, um den Web-Service auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzusehen.
