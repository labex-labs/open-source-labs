# Schaltfläche

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Um eine Schaltflächenkomponente zu rendern, folgen Sie diesen Schritten:

1. Verwenden Sie den `useState()`-Hook, um die `isToggledOn`-Zustandsvariable auf `defaultToggled` zu initialisieren.
2. Rendern Sie ein `<input>`-Element und binden Sie sein `onClick`-Ereignis, um die `isToggledOn`-Zustandsvariable zu aktualisieren. Wenden Sie die passende `className` auf das umgebende `<label>`-Element an.
3. Verwenden Sie die folgende CSS, um die Schaltflächenkomponente zu gestalten:

```css
.toggle input[type="checkbox"] {
  display: none;
}

.toggle.on {
  background-color: green;
}

.toggle.off {
  background-color: red;
}
```

Hier ist der Code:

```jsx
const Toggle = ({ defaultToggled = false }) => {
  const [isToggleOn, setIsToggleOn] = React.useState(defaultToggled);

  return (
    <label className={isToggleOn ? "toggle on" : "toggle off"}>
      <input
        type="checkbox"
        checked={isToggleOn}
        onChange={() => setIsToggleOn(!isToggleOn)}
      />
      {isToggleOn ? "ON" : "OFF"}
    </label>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Toggle />);
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
