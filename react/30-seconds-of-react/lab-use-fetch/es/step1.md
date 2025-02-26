# React useFetch Hook

> `index.html` y `script.js` ya se han proporcionado en la VM. En general, solo es necesario agregar código a `script.js` y `style.css`.

Aquí está el código:

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

Explicación:

- El propósito del código es implementar una llamada `fetch()` de manera declarativa utilizando hooks de React.
- El hook `useFetch` toma dos parámetros: una `url` y un objeto `options`.
- El hook inicializa tres variables de estado utilizando el hook `useState()`: `response`, `error` y `abort`.
- El hook `useEffect()` se utiliza para llamar asincrónicamente a `fetch()` y actualizar las variables de estado en consecuencia.
- Un `AbortController` se utiliza para permitir abortar la solicitud, y se utiliza para cancelar la solicitud cuando el componente se desmonta.
- El hook devuelve un objeto que contiene las variables de estado `response`, `error` y `abort`.
- El componente `ImageFetch` utiliza el hook `useFetch` para obtener una imagen aleatoria de un perro y mostrarla en un elemento `<img>`.

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
