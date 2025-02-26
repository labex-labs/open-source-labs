# React useToggler-Hook

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Um eine boolesche Zustandsvariable zu erstellen, die zwischen ihren beiden Zuständen umgeschaltet werden kann, folgen Sie diesen Schritten:

1. Verwenden Sie den `useState()`-Hook, um die `value`-Zustandsvariable und ihren Setter zu erstellen.
2. Erstellen Sie eine Funktion, die den Wert der `value`-Zustandsvariable umschaltet, und memoisiert sie mit dem `useCallback()`-Hook.
3. Geben Sie die `value`-Zustandsvariable und die memoisierte Umschaltfunktion zurück.

Hier ist eine Beispielimplementierung:

```jsx
const useToggler = (initialState) => {
  const [value, setValue] = React.useState(initialState);

  const toggleValue = React.useCallback(() => setValue((prev) => !prev), []);

  return [value, toggleValue];
};
```

Sie können diesen Hook dann in Ihren Komponenten verwenden, wie folgt:

```jsx
const Switch = () => {
  const [val, toggleVal] = useToggler(false);
  return <button onClick={toggleVal}>{val ? "ON" : "OFF"}</button>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Switch />);
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
