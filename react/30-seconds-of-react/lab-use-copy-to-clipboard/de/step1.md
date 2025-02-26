# React useCopyToClipboard-Hook

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Um den angegebenen Text in die Zwischenablage zu kopieren, verwenden Sie den in `/js/s/copy-to-clipboard/` bereitgestellten Codeausschnitt `copyToClipboard` zusammen mit dem `useState()`-Hook, um die Variable `copied` zu initialisieren. Um einen Callback für die `copyToClipboard`-Methode zu erstellen, verwenden Sie den `useCallback()`-Hook. Um den Zustandsvariablen `copied` zurückzusetzen, wenn sich der `text` ändert, verwenden Sie den `useEffect()`-Hook. Am Ende geben Sie die Zustandsvariable `copied` und den `copy`-Callback zurück.

Der folgende Code zeigt ein Beispiel dafür, wie diese Hooks und Methoden verwendet werden, um einen `TextCopy`-Komponenten zu erstellen. Wenn der Benutzer auf die Schaltfläche "Click to copy" klickt, wird die `copy`-Funktion aufgerufen und die Variable `copied` wird auf `true` gesetzt. Wenn die Kopie erfolgreich ist, wird "Copied!" angezeigt.

```jsx
const useCopyToClipboard = (text) => {
  const copyToClipboard = (str) => {
    const el = document.createElement("textarea");
    el.value = str;
    el.setAttribute("readonly", "");
    el.style.position = "absolute";
    el.style.left = "-9999px";
    document.body.appendChild(el);
    const selected =
      document.getSelection().rangeCount > 0
        ? document.getSelection().getRangeAt(0)
        : false;
    el.select();
    const success = document.execCommand("copy");
    document.body.removeChild(el);
    if (selected) {
      document.getSelection().removeAllRanges();
      document.getSelection().addRange(selected);
    }
    return success;
  };

  const [copied, setCopied] = React.useState(false);

  const copy = React.useCallback(() => {
    if (!copied) setCopied(copyToClipboard(text));
  }, [text]);

  React.useEffect(() => () => setCopied(false), [text]);

  return [copied, copy];
};

const TextCopy = (props) => {
  const [copied, copy] = useCopyToClipboard("Lorem ipsum");

  return (
    <div>
      <button onClick={copy}>Click to copy</button>
      <span>{copied && "Copied!"}</span>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<TextCopy />);
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
