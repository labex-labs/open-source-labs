# React usePortal-Hook

> `index.html` und `script.js` wurden bereits in der VM bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Um ein Portal zu erstellen, das Kinder außerhalb der Elternkomponente rendert, folgen Sie diesen Schritten:

1. Verwenden Sie den `useState()`-Hook, um eine Zustandsvariable zu erstellen, die die `render()`- und `remove()`-Funktionen für das Portal enthält.
2. Verwenden Sie `ReactDOM.createPortal()` und `ReactDOM.unmountComponentAtNode()`, um ein Portal und eine Funktion zum Entfernen davon zu erstellen. Verwenden Sie den `useCallback()`-Hook, um diese Funktionen als `createPortal()` zu umschließen und zu memoize.
3. Verwenden Sie den `useEffect()`-Hook, um `createPortal()` aufzurufen und die Zustandsvariable jedes Mal zu aktualisieren, wenn sich der Wert von `el` ändert.
4. Schließlich geben Sie die `render()`-Funktion der Zustandsvariable zurück.

Hier ist eine Beispielimplementierung:

```jsx
const usePortal = (el) => {
  const [portal, setPortal] = React.useState({
    render: () => null,
    remove: () => null
  });

  const createPortal = React.useCallback((el) => {
    const Portal = ({ children }) => ReactDOM.createPortal(children, el);
    const remove = () => ReactDOM.unmountComponentAtNode(el);
    return { render: Portal, remove };
  }, []);

  React.useEffect(() => {
    if (el) portal.remove();
    const newPortal = createPortal(el);
    setPortal(newPortal);
    return () => newPortal.remove(el);
  }, [el]);

  return portal.render;
};
```

Um diesen Hook zu verwenden, erstellen Sie eine Komponente, die `usePortal()` mit dem gewünschten DOM-Element als Argument aufruft. Diese Komponente kann dann die zurückgegebene `render()`-Funktion verwenden, um Inhalte im Portal zu rendern:

```jsx
const App = () => {
  const Portal = usePortal(document.querySelector("title"));

  return (
    <p>
      Hello world!
      <Portal>Portalized Title</Portal>
    </p>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
