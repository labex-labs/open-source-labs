# E-Mail-Link

> `index.html` und `script.js` wurden bereits in der virtuellen Maschine (VM) bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Diese Funktion erstellt einen Link, der beim Klicken den E-Mail-Client des Benutzers öffnet und eine neue E-Mail mit einem angegebenen Betreff und Inhalt füllt. Der Link wird mithilfe des `mailto:`-Protokolls formatiert.

Um die Funktion zu verwenden, geben Sie einen `email`-Prop mit der E-Mail-Adresse des Empfängers an und optional `subject`- und `body`-Props, um die E-Mail mit einem Anfangsinhalt zu füllen. Diese Props werden mithilfe von `encodeURIComponent` sicher codiert, bevor sie zur Link-URL hinzugefügt werden.

Der Link wird mit den bereitgestellten `children` als Inhalt gerendert.

```jsx
const Mailto = ({ email, subject = "", body = "", children }) => {
  const params =
    subject || body
      ? `?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(
          body
        )}`
      : "";

  return <a href={`mailto:${email}${params}`}>{children}</a>;
};
```

Beispiel für die Verwendung:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Mailto email="foo@bar.baz" subject="Hello & Welcome" body="Hello world!">
    Mail me!
  </Mailto>
);
```

Klicken Sie bitte auf 'Go Live' in der unteren rechten Ecke, um den Web-Service auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzusehen.
