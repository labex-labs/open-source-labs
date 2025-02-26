# React useIsomporphicEffect-Hook

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Um die richtige Verwendung von `useEffect()` auf dem Server und `useLayoutEffect()` auf dem Client sicherzustellen, können Sie `typeof` verwenden, um zu überprüfen, ob das `Window`-Objekt definiert ist. Wenn ja, geben Sie `useLayoutEffect()` zurück, andernfalls `useEffect()`. Hier ist ein Beispiel dafür, wie dies implementiert werden kann:

```jsx
const useIsomorphicEffect =
  typeof window !== "undefined" ? React.useLayoutEffect : React.useEffect;
```

Dann können Sie in Ihrem Code `useIsomorphicEffect()` wie in diesem Beispiel verwenden:

```jsx
const MyApp = () => {
  useIsomorphicEffect(() => {
    window.console.log("Hello");
  }, []);

  return null;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Dies wird 'Hello' in der Konsole ausgeben, wenn die Komponente gemountet wird, und funktioniert sowohl auf dem Server als auch auf dem Client korrekt.

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite zu previewen.
