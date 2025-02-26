# React useRequestAnimationFrame-Hook

> `index.html` und `script.js` wurden bereits in der VM bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Um eine animierende Funktion vor jedem Neuzeichnen auszuführen, verwenden Sie den `useRef()`-Hook, um `requestRef` und `previousTimeRef`-Variablen zu erstellen. Definieren Sie dann eine `animate()`-Funktion, die diese Variablen aktualisiert, die `callback`-Funktion ausführt und `Window.requestAnimationFrame()` ständig aufruft. Schließlich verwenden Sie den `useEffect()`-Hook mit einem leeren Array, um den Wert von `requestRef` mit `Window.requestAnimationFrame()` zu initialisieren, und verwenden den zurückgegebenen Wert und `Window.cancelAnimationFrame()`, um aufzuräumen, wenn die Komponente entladen wird.

Hier ist eine Beispielimplementierung von `useRequestAnimationFrame()`:

```jsx
const useRequestAnimationFrame = (callback) => {
  const requestRef = React.useRef();
  const previousTimeRef = React.useRef();

  const animate = (time) => {
    if (previousTimeRef.current) {
      callback(time - previousTimeRef.current);
    }
    previousTimeRef.current = time;
    requestRef.current = requestAnimationFrame(animate);
  };

  React.useEffect(() => {
    requestRef.current = requestAnimationFrame(animate);
    return () => cancelAnimationFrame(requestRef.current);
  }, []);
};
```

Um diesen benutzerdefinierten Hook in einer Komponente zu verwenden, übergeben Sie einfach eine Callback-Funktion. Beispielsweise um einen einfachen Zähler zu erstellen, der mit 100 FPS aktualisiert wird:

```jsx
const Counter = () => {
  const [count, setCount] = React.useState(0);

  useRequestAnimationFrame((deltaTime) => {
    setCount((prevCount) => (prevCount + deltaTime * 0.01) % 100);
  });

  return <p>{Math.round(count)}</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Counter />);
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
