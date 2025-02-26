# Lazy-Laden von Bildern

> `index.html` und `script.js` wurden bereits in der VM bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Um ein Bild zu rendern, das das Lazy Loading unterstützt, folgen Sie diesen Schritten:

1. Verwenden Sie den `useState()`-Hook, um einen zustandsbehafteten Wert zu erstellen, der angibt, ob das Bild geladen wurde.
2. Verwenden Sie den `useEffect()`-Hook, um zu überprüfen, ob `HTMLImageElement.prototype` `'loading'` enthält. Dies überprüft, ob das Lazy Loading nativ unterstützt wird. Wenn nicht, erstellen Sie einen neuen `IntersectionObserver` und verwenden Sie `IntersectionObserver.observer()`, um das `<img>`-Element zu beobachten. Verwenden Sie den Rückgabewert des Hooks, um aufzuräumen, wenn die Komponente abmontiert wird.
3. Verwenden Sie den `useCallback()`-Hook, um eine Callback-Funktion für den `IntersectionObserver` zu memoize. Diese Callback-Funktion wird den `isLoaded`-Zustandsvariablen aktualisieren und `IntersectionObserver.disconnect()` verwenden, um die `IntersectionObserver`-Instanz zu trennen.
4. Verwenden Sie den `useRef()`-Hook, um zwei Refs zu erstellen. Eine wird das `<img>`-Element halten und die andere die `IntersectionObserver`-Instanz, wenn erforderlich.
5. Schließlich rendern Sie das `<img>`-Element mit den angegebenen Attributen. Wenden Sie `loading='lazy'` an, um es lazily zu laden, wenn erforderlich. Verwenden Sie `isLoaded`, um den Wert des `src`-Attributs zu bestimmen.

Hier ist eine Beispielimplementierung dieser Schritte:

```jsx
const LazyLoadImage = ({
  alt,
  src,
  className,
  loadInitially = false,
  observerOptions = { root: null, rootMargin: "200px 0px" },
  ...props
}) => {
  const observerRef = React.useRef(null);
  const imgRef = React.useRef(null);
  const [isLoaded, setIsLoaded] = React.useState(loadInitially);

  const observerCallback = React.useCallback(
    (entries) => {
      if (entries[0].isIntersecting) {
        observerRef.current.disconnect();
        setIsLoaded(true);
      }
    },
    [observerRef]
  );

  React.useEffect(() => {
    if (loadInitially) return;

    if ("loading" in HTMLImageElement.prototype) {
      setIsLoaded(true);
      return;
    }

    observerRef.current = new IntersectionObserver(
      observerCallback,
      observerOptions
    );
    observerRef.current.observe(imgRef.current);
    return () => {
      observerRef.current.disconnect();
    };
  }, []);

  return (
    <img
      alt={alt}
      src={isLoaded ? src : ""}
      ref={imgRef}
      className={className}
      loading={loadInitially ? undefined : "lazy"}
      {...props}
    />
  );
};
```

Um diese `LazyLoadImage`-Komponente zu verwenden, rufen Sie sie einfach mit den `src`- und `alt`-Attributen des Bilds auf:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <LazyLoadImage src="https://picsum.photos/id/1080/600/600" alt="Erdbeeren" />
);
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite zu previewen.
