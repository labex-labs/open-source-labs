# React useFetch Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Voici le code :

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
    return <div>Chargement...</div>;
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

Explication :

- Le but du code est d'implémenter un appel `fetch()` de manière déclarative à l'aide de hooks React.
- Le hook `useFetch` prend deux paramètres : une `url` et un objet `options`.
- Le hook initialise trois variables d'état à l'aide du hook `useState()` : `response`, `error` et `abort`.
- Le hook `useEffect()` est utilisé pour appeler asynchronement `fetch()` et mettre à jour les variables d'état en conséquence.
- Un `AbortController` est utilisé pour permettre d'annuler la requête, et il est utilisé pour annuler la requête lorsque le composant est démonté.
- Le hook renvoie un objet contenant les variables d'état `response`, `error` et `abort`.
- Le composant `ImageFetch` utilise le hook `useFetch` pour récupérer une image de chien aléatoire et l'afficher dans un élément `<img>`.

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
