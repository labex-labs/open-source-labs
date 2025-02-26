# React useOnWindowScroll-Hook

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Diese Funktion führt eine Callback-Funktion aus, jedes Mal wenn das Fenster scrollt. Um es zu implementieren:

1. Verwenden Sie den `useRef()`-Hook, um eine Referenzvariable `listener` zu erstellen.
2. Verwenden Sie den `useEffect()`-Hook und `EventTarget.addEventListener()`, um auf das `'scroll'`-Ereignis des `Window`-Objekts zu hören und die Listener-Referenz an `listener.current` zuzuweisen.
3. Verwenden Sie `EventTarget.removeEventListener()`, um alle vorhandenen Listener zu entfernen, wenn die Komponente entladen wird.

Hier ist der Code:

```jsx
const useOnWindowScroll = (callback) => {
  const listener = React.useRef(null);

  React.useEffect(() => {
    if (listener.current) {
      window.removeEventListener("scroll", listener.current);
    }
    listener.current = () => {
      callback(window.pageYOffset);
    };
    window.addEventListener("scroll", listener.current);
    return () => {
      window.removeEventListener("scroll", listener.current);
    };
  }, [callback]);
};
```

Um die Funktion zu testen, können Sie sie in einer Komponente wie folgt verwenden:

```jsx
const App = () => {
  useOnWindowScroll((scrollY) => console.log(`scroll Y: ${scrollY}`));
  return <p style={{ height: "300vh" }}>Scroll and check the console</p>;
};

ReactDOM.render(<App />, document.getElementById("root"));
```

Dies wird die vertikale Scrollposition des Fensters jedes Mal ausgeben, wenn es gescrollt wird.

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
