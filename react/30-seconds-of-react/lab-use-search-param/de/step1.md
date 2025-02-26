# React useSearchParam-Hook

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Führen Sie die folgenden Schritte aus, um die Suchparameter der Browseradresse zu verfolgen:

1. Erstellen Sie einen Callback mit dem `useCallback()`-Hook. Der Callback sollte den `URLSearchParams`-Konstruktor verwenden, um den aktuellen Wert des gewünschten Parameters abzurufen.

```jsx
const getValue = React.useCallback(
  () => new URLSearchParams(window.location.search).get(param),
  [param]
);
```

2. Erstellen Sie eine Zustandsvariable, die den aktuellen Wert des Parameters enthält, mit dem `useState()`-Hook.

```jsx
const [value, setValue] = React.useState(getValue);
```

3. Legen Sie geeignete Ereignislistener fest, um die Zustandsvariable beim Mounting zu aktualisieren und sie beim Entfernen zu bereinigen, indem Sie den `useEffect()`-Hook verwenden.

```jsx
React.useEffect(() => {
  const onChange = () => {
    setValue(getValue());
  };

  window.addEventListener("popstate", onChange);
  window.addEventListener("pushstate", onChange);
  window.addEventListener("replacestate", onChange);

  return () => {
    window.removeEventListener("popstate", onChange);
    window.removeEventListener("pushstate", onChange);
    window.removeEventListener("replacestate", onChange);
  };
}, []);
```

Hier ist ein Beispiel dafür, wie Sie diesen benutzerdefinierten Hook in einem Komponenten verwenden:

```jsx
const MyApp = () => {
  const post = useSearchParam("post");

  return (
    <>
      <p>Post-Param-Wert: {post || "null"}</p>
      <button
        onClick={() =>
          history.pushState({}, "", location.pathname + "?post=42")
        }
      >
        Post 42 anzeigen
      </button>
      <button onClick={() => history.pushState({}, "", location.pathname)}>
        Beenden
      </button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

In diesem Beispiel wird eine `MyApp`-Komponente erstellt, die den benutzerdefinierten `useSearchParam`-Hook verwendet, um den Wert des `post`-Parameters in der Suchleiste der Adresse zu verfolgen. Der `post`-Wert wird in einem Absatztag angezeigt. Zwei Schaltflächen sind ebenfalls enthalten, um zu demonstrieren, wie der Wert des Suchparameters der Adresse geändert werden kann.

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
