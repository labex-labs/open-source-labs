# Schließbare Warnung (Closable Alert)

> `index.html` und `script.js` wurden bereits in der virtuellen Maschine (VM) bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Rendert eine Warnungskomponente (Alert component) mit der Prop `type`.

Die `Alert`-Komponente akzeptiert die folgenden Props:

- `isDefaultShown`: Ein boolescher Wert, der bestimmt, ob die Warnung zunächst angezeigt wird oder nicht (Standardwert ist `false`).
- `timeout`: Eine Zahl, die die Dauer in Millisekunden angibt, bevor die Warnung ausblendet (Standardwert ist `250`).
- `type`: Ein String, der den Typ der Warnung bestimmt (z.B. "warning", "error", "info").
- `message`: Ein String, der die anzuzeigende Nachricht in der Warnung enthält.

Die Komponente führt die folgenden Aktionen aus:

- Verwendet den `useState()`-Hook, um die Zustandsvariablen `isShown` und `isLeaving` zu erstellen und beide zunächst auf `false` zu setzen.
- Definiert eine Variable `timeoutId`, um die Timer-Instanz zu speichern, um sie beim Entfernen der Komponente zu löschen.
- Verwendet den `useEffect()`-Hook, um den Wert von `isShown` auf `true` zu aktualisieren und das Intervall mithilfe von `timeoutId` zu löschen, wenn die Komponente entfernt wird.
- Definiert eine Funktion `closeAlert`, um die Komponente aus dem DOM zu entfernen, indem eine Ausblendanimation angezeigt wird und `isShown` über `setTimeout()` auf `false` gesetzt wird.
- Rendert die Warnungskomponente, wenn `isShown` `true` ist. Die Komponente hat die entsprechenden Stile basierend auf der Prop `type` und blendet aus, wenn `isLeaving` `true` ist.

Hier ist der Code:

```css
@keyframes leave {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}

.alert {
  padding: 0.75rem 0.5rem;
  margin-bottom: 0.5rem;
  text-align: left;
  padding-right: 40px;
  border-radius: 4px;
  font-size: 16px;
  position: relative;
}

.alert.warning {
  color: #856404;
  background-color: #fff3cd;
  border-color: #ffeeba;
}

.alert.error {
  color: #721c24;
  background-color: #f8d7da;
  border-color: #f5c6cb;
}

.alert.leaving {
  animation: leave 0.5s forwards;
}

.alert.close {
  position: absolute;
  top: 0;
  right: 0;
  padding: 0 0.75rem;
  color: #333;
  border: 0;
  height: 100%;
  cursor: pointer;
  background: none;
  font-weight: 600;
  font-size: 16px;
}

.alert.close::after {
  content: "x";
}
```

```jsx
const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
  const [isShown, setIsShown] = React.useState(isDefaultShown);
  const [isLeaving, setIsLeaving] = React.useState(false);

  let timeoutId = null;

  React.useEffect(() => {
    setIsShown(true);
    return () => {
      clearTimeout(timeoutId);
    };
  }, [isDefaultShown, timeout, timeoutId]);

  const closeAlert = () => {
    setIsLeaving(true);
    timeoutId = setTimeout(() => {
      setIsLeaving(false);
      setIsShown(false);
    }, timeout);
  };

  return (
    isShown && (
      <div
        className={`alert ${type} ${isLeaving ? "leaving" : ""}`}
        role="alert"
      >
        <button className="close" onClick={closeAlert} />
        {message}
      </div>
    )
  );
};
```

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Alert type="info" message="This is info" />
);
```

Klicken Sie bitte auf 'Go Live' in der unteren rechten Ecke, um den Web-Service auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzusehen.
