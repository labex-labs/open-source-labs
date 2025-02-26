# Carousel

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Ce code affiche un composant carousel. Voici les étapes qu'il suit :

1. Il utilise le hook `useState()` pour créer la variable d'état `active` et l'initialise à `0` (l'index du premier élément du carousel).
2. Il utilise le hook `useEffect()` pour configurer un minuteur avec `setTimeout()`. Lorsque le minuteur expire, il met à jour la valeur de `active` avec l'index de l'élément suivant dans le carousel (en utilisant l'opérateur modulo pour revenir au début si nécessaire). Il nettoie également le minuteur lorsque le composant est démonté.
3. Il calcule la `className` pour chaque élément du carousel en les parcourant et en appliquant la classe appropriée en fonction de savoir si l'élément est actuellement actif ou non.
4. Il affiche les éléments du carousel à l'aide de `React.cloneElement()`, en passant tous les autres props à l'aide de `...rest`, et en ajoutant la `className` calculée à chaque élément.

Les styles CSS définissent la disposition du carousel et de ses éléments. Le conteneur du carousel a `position: relative`, tandis que les éléments ont `position: absolute` et `visibility: hidden` par défaut. Lorsqu'un élément est actif, il reçoit une classe `visible`, qui définit sa `visibility` sur `visible`.

```css
.carousel {
  position: relative;
}

.carousel-item {
  position: absolute;
  visibility: hidden;
}

.carousel-item.visible {
  visibility: visible;
}
```

Voici le code complet :

```jsx
const Carousel = ({ carouselItems, ...rest }) => {
  const [active, setActive] = React.useState(0);
  let scrollInterval = null;

  React.useEffect(() => {
    scrollInterval = setTimeout(() => {
      setActive((active + 1) % carouselItems.length);
    }, 2000);
    return () => clearTimeout(scrollInterval);
  });

  return (
    <div className="carousel">
      {carouselItems.map((item, index) => {
        const activeClass = active === index ? " visible" : "";
        return React.cloneElement(item, {
          ...rest,
          className: `carousel-item${activeClass}`
        });
      })}
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <Carousel
    carouselItems={[
      <div>carousel item 1</div>,
      <div>carousel item 2</div>,
      <div>carousel item 3</div>
    ]}
  />
);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
