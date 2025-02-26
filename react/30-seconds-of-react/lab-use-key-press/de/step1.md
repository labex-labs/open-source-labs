# React useKeyPress-Hook

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Diese Funktion überwacht Änderungen im gedrückten Zustand einer bestimmten Taste. Um sie zu verwenden:

- Rufen Sie `useKeyPress()` mit der Ziel-Taste als Argument auf.
- `useKeyPress()` gibt einen booleschen Wert zurück, der angibt, ob die Taste derzeit gedrückt ist.
- Die Funktion verwendet den `useState()`-Hook, um eine Zustandsvariable zu erstellen, die den gedrückten Zustand der angegebenen Taste aufnimmt.
- Sie definiert zwei Handler-Funktionen, die die Zustandsvariable entsprechend beim Drücken oder Loslassen der Taste aktualisieren.
- Der `useEffect()`-Hook und `EventTarget.addEventListener()` werden verwendet, um die `'keydown'`- und `'keyup'`-Ereignisse zu behandeln.
- Schließlich wird `EventTarget.removeEventListener()` verwendet, um die Bereinigung durchzuführen, nachdem die Komponente abgemounted wurde.

```jsx
const useKeyPress = (targetKey) => {
  const [isKeyPressed, setKeyPressed] = React.useState(false);

  const handleKeyDown = ({ key }) => {
    if (key === targetKey) setKeyPressed(true);
  };

  const handleKeyUp = ({ key }) => {
    if (key === targetKey) setKeyPressed(false);
  };

  React.useEffect(() => {
    window.addEventListener("keydown", handleKeyDown);
    window.addEventListener("keyup", handleKeyUp);

    return () => {
      window.removeEventListener("keydown", handleKeyDown);
      window.removeEventListener("keyup", handleKeyUp);
    };
  }, [targetKey]);

  return isKeyPressed;
};
```

Hier ist ein Beispiel für die Verwendung von `useKeyPress()` in einer React-Komponente:

```jsx
const MyApp = () => {
  const isWKeyPressed = useKeyPress("w");

  return <p>The "w" key is {!isWKeyPressed ? "not " : ""}pressed!</p>;
};

ReactDOM.render(<MyApp />, document.getElementById("root"));
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
