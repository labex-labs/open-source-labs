# React useFetch-Hook

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Hier ist der Code:

```jsx
const useFetch = (url, options) => {
  const [response, setResponse] = React.useState(null);
  const [error, setError] = React.useState(null);
  const [abort, setAbort] = React.useState(() => {});

  React.useEffect(() => {
    const abortController = new AbortController();
    const signal = abortController.signal;

    const fetchData = async () => {
      try {
        const res = await fetch(url, { ...options, signal });
        const json = await res.json();
        setResponse(json);
      } catch (error) {
        setError(error);
      }
    };
    fetchData();

    return () => {
      abort();
    };
  }, []);

  return { response, error, abort };
};

const ImageFetch = (props) => {
  const res = useFetch("https://dog.ceo/api/breeds/image/random", {});

  if (!res.response) {
    return <div>Loading...</div>;
  }

  const imageUrl = res.response.message;

  return (
    <div>
      <img src={imageUrl} alt="avatar" width={400} height="auto" />
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<ImageFetch />);
```

Erklärung:

- Der Zweck des Codes ist es, einen `fetch()`-Aufruf auf deklarative Weise mit React-Hooks zu implementieren.
- Der `useFetch`-Hook nimmt zwei Parameter: eine `url` und ein `options`-Objekt.
- Der Hook initialisiert drei Zustandsvariablen mit dem `useState()`-Hook: `response`, `error` und `abort`.
- Der `useEffect()`-Hook wird verwendet, um `fetch()` asynchron aufzurufen und die Zustandsvariablen entsprechend zu aktualisieren.
- Ein `AbortController` wird verwendet, um das Abbrechen der Anfrage zu ermöglichen, und es wird verwendet, um die Anfrage abzubrechen, wenn die Komponente entladen wird.
- Der Hook gibt ein Objekt zurück, das die `response`, `error` und `abort` Zustandsvariablen enthält.
- Die `ImageFetch`-Komponente verwendet den `useFetch`-Hook, um ein zufälliges Hundefoto abzurufen und es in einem `<img>`-Element anzuzeigen.

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
