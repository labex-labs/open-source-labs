# React useIntersectionObserver Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Pour observer les changements de visibilité d'un élément donné, suivez ces étapes :

1. Utilisez le hook `useState()` pour stocker la valeur d'intersection de l'élément donné.
2. Créez un `IntersectionObserver` avec les `options` données et une callback appropriée pour mettre à jour la variable d'état `isIntersecting`.
3. Utilisez le hook `useEffect()` pour appeler `IntersectionObserver.observe()` lors du montage du composant et nettoyer en utilisant `IntersectionObserver.unobserve()` lors du démontage.

Voici une implémentation d'exemple :

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

Vous pouvez utiliser le hook `useIntersectionObserver` comme ceci :

```jsx
const MyApp = () => {
  const ref = React.useRef();
  const onScreen = useIntersectionObserver(ref, { threshold: 0.5 });

  return (
    <div>
      <div style={{ height: "100vh" }}>Scroll down</div>
      <div style={{ height: "100vh" }} ref={ref}>
        <p>{onScreen ? "Element is on screen." : "Scroll more!"}</p>
      </div>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
