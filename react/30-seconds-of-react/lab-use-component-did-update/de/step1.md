# React useComponentDidUpdate Hook

> `index.html` und `script.js` wurden bereits in der VM bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Dieser Code stellt einen benutzerdefinierten Hook namens `useComponentDidUpdate` zur Verfügung, der eine bereitgestellte `callback`-Funktion jedes Mal ausführt, wenn eine Komponente aktualisiert wird. Hier sind die Schritte, die der Hook folgt:

1. Erstellen Sie eine Variable `mounted` mithilfe des Hooks `useRef()`. Diese Variable verfolgt, ob die Komponente bereits gemountet wurde oder nicht.
2. Verwenden Sie den Hook `useEffect()`, um den Wert von `mounted` beim ersten Ausführen des Hooks auf `true` zu setzen.
3. Bei nachfolgenden Ausführungen des Hooks wird die bereitgestellte `callback`-Funktion nur ausgeführt, wenn die Komponente bereits gemountet ist.
4. Wenn ein zweiter Argument `condition` bereitgestellt wird, wird der Hook nur ausgeführt, wenn eine seiner Abhängigkeiten sich ändert.
5. Dieser Hook verhält sich wie die Lebenszyklusmethode `componentDidUpdate()` von Klassenkomponenten.

Hier ist der Code:

```jsx
const useComponentDidUpdate = (callback, condition) => {
  const isMounted = React.useRef(false);
  React.useEffect(() => {
    if (isMounted.current) {
      callback();
    } else {
      isMounted.current = true;
    }
  }, condition);
};

const App = () => {
  const [value, setValue] = React.useState(0);
  const [otherValue, setOtherValue] = React.useState(1);

  useComponentDidUpdate(() => {
    console.log(`Current value is ${value}.`);
  }, [value]);

  return (
    <>
      <p>
        Value: {value}, other value: {otherValue}
      </p>
      <button onClick={() => setValue(value + 1)}>Increment value</button>
      <button onClick={() => setOtherValue(otherValue + 1)}>
        Increment other value
      </button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
