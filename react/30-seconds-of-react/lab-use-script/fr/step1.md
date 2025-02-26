# React useScript Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Pour charger dynamiquement un script externe, utilisez le hook `useState()` pour créer une variable d'état qui stocke l'état de chargement du script. Ensuite, utilisez le hook `useEffect()` pour gérer toute la logique de chargement et de déchargement du script à chaque fois que la valeur de `src` change. Si aucune valeur de `src` n'est présente, définissez le `status` sur `'idle'` et retournez. Utilisez `Document.querySelector()` pour vérifier si un élément `<script>` avec la valeur de `src` appropriée existe. Si aucun élément pertinent n'existe, utilisez `Document.createElement()` pour en créer un et lui donner les attributs appropriés. Utilisez l'attribut `data-status` comme moyen d'indiquer l'état du script, en le définissant initialement sur `'loading'`. Si un élément pertinent existe, passez l'initialisation et mettez à jour le `status` à partir de son attribut `data-status`. Cela garantit qu'aucun élément dupliqué ne sera créé. Utilisez `EventTarget.addEventListener()` pour écouter les événements `'load'` et `'error'` et les gérer en mettant à jour l'attribut `data-status` et la variable d'état `status`. Enfin, lorsque le composant est démonté, utilisez `Document.removeEventListener()` pour supprimer tous les écouteurs liés à l'élément.

Voici une implémentation exemple du hook `useScript`:

```jsx
const useScript = (src) => {
  const [status, setStatus] = React.useState(src ? "loading" : "idle");

  React.useEffect(() => {
    if (!src) {
      setStatus("idle");
      return;
    }

    let script = document.querySelector(`script[src="${src}"]`);

    if (!script) {
      script = document.createElement("script");
      script.src = src;
      script.async = true;
      script.setAttribute("data-status", "loading");
      document.body.appendChild(script);

      const setDataStatus = (event) => {
        script.setAttribute(
          "data-status",
          event.type === "load" ? "ready" : "error"
        );
      };
      script.addEventListener("load", setDataStatus);
      script.addEventListener("error", setDataStatus);
    } else {
      setStatus(script.getAttribute("data-status"));
    }

    const setStateStatus = (event) => {
      setStatus(event.type === "load" ? "ready" : "error");
    };

    script.addEventListener("load", setStateStatus);
    script.addEventListener("error", setStateStatus);

    return () => {
      if (script) {
        script.removeEventListener("load", setStateStatus);
        script.removeEventListener("error", setStateStatus);
      }
    };
  }, [src]);

  return status;
};
```

Voici un exemple d'utilisation du hook `useScript`:

```jsx
const script =
  "data:text/plain;charset=utf-8;base64,KGZ1bmN0aW9uKCl7IGNvbnNvbGUubG9nKCdIZWxsbycpIH0pKCk7";

const Child = () => {
  const status = useScript(script);
  return <p>Child status: {status}</p>;
};

const MyApp = () => {
  const status = useScript(script);
  return (
    <>
      <p>Parent status: {status}</p>
      <Child />
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
