# React useHover Hook

> `index.html` und `script.js` wurden bereits in der VM bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Dieser Code erstellt einen benutzerdefinierten Hook, der das Überlagern über eine umschlossene Komponente behandelt.

Um den Hook zu verwenden:

- Verwenden Sie `useState()`, um eine Variable zu erstellen, die den Überlagerungszustand aufnimmt.
- Verwenden Sie `useCallback()`, um zwei Handlerfunktionen zu memoize, die den Zustand aktualisieren.
- Verwenden Sie `useCallback()`, um einen Callback-Ref zu erstellen und die Listener für die `'mouseover'`- und `'mouseout'`-Ereignisse zu erstellen oder zu aktualisieren.
- Verwenden Sie `useRef()`, um den letzten Knoten zu verfolgen, der an `callbackRef` übergeben wurde, um seine Listener entfernen zu können.

```jsx
const useHover = () => {
  const [isHovering, setIsHovering] = React.useState(false);
  const handleMouseOver = React.useCallback(() => setIsHovering(true), []);
  const handleMouseOut = React.useCallback(() => setIsHovering(false), []);
  const nodeRef = React.useRef();
  const callbackRef = React.useCallback(
    (node) => {
      if (nodeRef.current) {
        nodeRef.current.removeEventListener("mouseover", handleMouseOver);
        nodeRef.current.removeEventListener("mouseout", handleMouseOut);
      }
      nodeRef.current = node;
      if (nodeRef.current) {
        nodeRef.current.addEventListener("mouseover", handleMouseOver);
        nodeRef.current.addEventListener("mouseout", handleMouseOut);
      }
    },
    [handleMouseOver, handleMouseOut]
  );

  return [callbackRef, isHovering];
};
```

Dies ist ein Beispiel für die Verwendung des Hooks:

```jsx
const MyApp = () => {
  const [hoverRef, isHovering] = useHover();
  return <div ref={hoverRef}>{isHovering ? "Hovering" : "Not hovering"}</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
