# React useEffectOnce-Hook

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Der folgende Code implementiert eine Funktion `useEffectOnce(callback, when)`, die eine `callback`-Funktion nur einmal ausführt, wenn eine `when`-Bedingung wahr wird.

Um diese Funktion zu implementieren:

- Erstellen Sie eine Variable `hasRunOnce` mithilfe des `useRef()`-Hooks, um den Ausführungsstatus des Effekts zu verfolgen.
- Verwenden Sie den `useEffect()`-Hook, der nur dann ausgeführt wird, wenn sich die `when`-Bedingung ändert.
- Innerhalb des `useEffect()`-Hooks überprüfen Sie, ob `when` `true` ist und der Effekt zuvor noch nicht ausgeführt wurde. Wenn beide Bedingungen erfüllt sind, führen Sie `callback` aus und legen Sie `hasRunOnce` auf `true` fest.

```jsx
const useEffectOnce = (callback, when) => {
  const hasRunOnce = React.useRef(false);
  React.useEffect(() => {
    if (when && !hasRunOnce.current) {
      callback();
      hasRunOnce.current = true;
    }
  }, [when]);
};
```

Hier ist ein Beispiel für die Verwendung von `useEffectOnce()`:

```jsx
const App = () => {
  const [clicked, setClicked] = React.useState(false);
  useEffectOnce(() => {
    console.log("mounted");
  }, clicked);
  return <button onClick={() => setClicked(true)}>Click me</button>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Im Beispiel wird `useEffectOnce()` verwendet, um "mounted" in der Konsole auszugeben, wenn der Button zum ersten Mal geklickt wird. Dem `useEffectOnce()`-Hook werden zwei Argumente übergeben: die auszuführende `callback`-Funktion und die zu überprüfende `when`-Bedingung. Die `when`-Bedingung ist auf den `clicked`-Zustand gesetzt, sodass die `callback`-Funktion nur ausgeführt wird, wenn `clicked` zum ersten Mal `true` ist.

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
