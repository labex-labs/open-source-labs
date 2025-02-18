# React useMutationObserver-Hook

> `index.html` und `script.js` wurden bereits in der virtuellen Maschine bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Um Änderungen am DOM-Baum zu überwachen, kann der `useMutationObserver`-Hook verwendet werden. So funktioniert es:

1. Der Hook nimmt drei Parameter entgegen: `ref`, `callback` und `options`.
2. Innerhalb des Hooks wird ein `useEffect()`-Hook verwendet, der von den Werten von `callback` und `options` abhängt.
3. Wenn die gegebene `ref` initialisiert ist, wird ein neuer `MutationObserver` erstellt und die `callback`-Funktion übergeben.
4. `MutationObserver.observe()` wird mit den angegebenen `options` aufgerufen, um die gegebene `ref` auf Änderungen zu überwachen.
5. `MutationObserver.disconnect()` wird verwendet, um den Beobachter von der `ref` zu entfernen, wenn die Komponente aus dem DOM entfernt wird.

Hier ist der Code:

```jsx
const useMutationObserver = (
  ref,
  callback,
  options = {
    attributes: true,
    characterData: true,
    childList: true,
    subtree: true
  }
) => {
  React.useEffect(() => {
    if (!ref.current) return;

    const observer = new MutationObserver(callback);
    observer.observe(ref.current, options);

    return () => observer.disconnect();
  }, [callback, options, ref]);
};
```

In der `App`-Komponente wird der `useMutationObserver`-Hook verwendet, um Änderungen am `mutationRef`-Element zu überwachen. Die `incrementMutationCount`-Funktion wird als `callback` übergeben.

```jsx
const App = () => {
  const mutationRef = React.useRef();
  const [mutationCount, setMutationCount] = React.useState(0);

  const incrementMutationCount = React.useCallback(() => {
    setMutationCount((count) => count + 1);
  }, []);

  useMutationObserver(mutationRef, incrementMutationCount);

  const [content, setContent] = React.useState("Hello world");

  return (
    <>
      <label htmlFor="content-input">Edit this to update the text:</label>
      <textarea
        id="content-input"
        style={{ width: "100%" }}
        value={content}
        onChange={(e) => setContent(e.target.value)}
      />
      <div style={{ width: "100%" }} ref={mutationRef}>
        <div
          style={{
            resize: "both",
            overflow: "auto",
            maxWidth: "100%",
            border: "1px solid black"
          }}
        >
          <h2>Resize or change the content:</h2>
          <p>{content}</p>
        </div>
      </div>
      <div>
        <h3>Mutation count {mutationCount}</h3>
      </div>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Klicken Sie unten rechts auf 'Go Live', um den Web-Service auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzusehen.
