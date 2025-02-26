# Passwort anzeigen/verbergen umschalten

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Der folgende Code rendert ein Passwort-Eingabefeld mit einem Entschlüsselungsbutton. Er verwendet den `useState()`-Hook, um die `shown`-Zustandsvariable zu erstellen und ihren Anfangswert auf `false` zu setzen. Wenn der `Anzeigen/Verbergen`-Button angeklickt wird, wird die `setShown`-Funktion aufgerufen, um den `type` des Inputs zwischen `'text'` und `'password'` umzuschalten.

```jsx
const PasswordRevealer = ({ value }) => {
  const [shown, setShown] = React.useState(false);
  return (
    <>
      <input type={shown ? "text" : "password"} value={value} />
      <button onClick={() => setShown(!shown)}>Anzeigen/Verbergen</button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <PasswordRevealer />
);
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
