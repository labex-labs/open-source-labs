# React useIntersectionObserver-Hook

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Um die Sichtbarkeitsänderungen eines bestimmten Elements zu beobachten, gehen Sie folgenschrittweise vor:

1. Verwenden Sie den `useState()`-Hook, um den Schnittwert des angegebenen Elements zu speichern.
2. Erstellen Sie einen `IntersectionObserver` mit den angegebenen `Optionen` und einem passenden Callback, um die `isIntersecting`-Zustandsvariable zu aktualisieren.
3. Verwenden Sie den `useEffect()`-Hook, um `IntersectionObserver.observe()` beim Mounten der Komponente aufzurufen und mit `IntersectionObserver.unobserve()` aufzuräumen, wenn die Komponente entladen wird.

Hier ist eine Beispielimplementierung:

```jsx
const useIntersectionObserver = (ref, options) => {
  const [isIntersecting, setIsIntersecting] = React.useState(false);

  React.useEffect(() => {
    const observer = new IntersectionObserver(([entry]) => {
      setIsIntersecting(entry.isIntersecting);
    }, options);

    if (ref.current) {
      observer.observe(ref.current);
    }

    return () => {
      observer.unobserve(ref.current);
    };
  }, [ref, options]);

  return isIntersecting;
};
```

Sie können den `useIntersectionObserver`-Hook wie folgt verwenden:

```jsx
const MyApp = () => {
  const ref = React.useRef();
  const onScreen = useIntersectionObserver(ref, { threshold: 0.5 });

  return (
    <div>
      <div style={{ height: "100vh" }}>Scroll runter</div>
      <div style={{ height: "100vh" }} ref={ref}>
        <p>{onScreen ? "Element ist auf dem Bildschirm." : "Scroll mehr!"}</p>
      </div>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
