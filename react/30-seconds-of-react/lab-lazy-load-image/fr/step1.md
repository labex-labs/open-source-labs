# Chargement différé d'images

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Pour afficher une image qui prend en charge le chargement différé, suivez ces étapes :

1. Utilisez le hook `useState()` pour créer une valeur avec état qui indique si l'image a été chargée.
2. Utilisez le hook `useEffect()` pour vérifier si `HTMLImageElement.prototype` contient `'loading'`. Cela vérifie si le chargement différé est pris en charge nativement. Si ce n'est pas le cas, créez un nouveau `IntersectionObserver` et utilisez `IntersectionObserver.observer()` pour observer l'élément `<img>`. Utilisez la valeur de retour du hook pour nettoyer lorsque le composant est démonté.
3. Utilisez le hook `useCallback()` pour mémoïser une fonction de rappel pour l'`IntersectionObserver`. Ce rappel mettra à jour la variable d'état `isLoaded` et utilisera `IntersectionObserver.disconnect()` pour déconnecter l'instance `IntersectionObserver`.
4. Utilisez le hook `useRef()` pour créer deux références. L'une contiendra l'élément `<img>` et l'autre l'instance `IntersectionObserver` si nécessaire.
5. Enfin, affichez l'élément `<img>` avec les attributs donnés. Appliquez `loading='lazy'` pour le charger de manière différée si nécessaire. Utilisez `isLoaded` pour déterminer la valeur de l'attribut `src`.

Voici une implémentation exemple de ces étapes :

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

Pour utiliser ce composant `LazyLoadImage`, appelez-le simplement avec les attributs `src` et `alt` de l'image :

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <LazyLoadImage
    src="https://picsum.photos/id/1080/600/600"
    alt="Strawberries"
  />
);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
