# Évaluation étoilée

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code dans `script.js` et `style.css`.

Créez un composant `Star` qui affiche chaque étoile individuelle avec l'apparence appropriée en fonction de l'état du composant parent. Ensuite, définissez un composant `StarRating` qui utilise le hook `useState()` pour définir les variables d'état `rating` et `selection` avec les valeurs initiales appropriées.

Dans `StarRating`, créez une méthode appelée `hoverOver` qui met à jour `selection` selon l'`événement` fourni. Si `événement` n'est pas fourni ou s'il est `null`, réinitialisez `selection` à `0`. Utilisez l'attribut `.data-star-id` de la cible de l'événement pour déterminer la valeur de `selection`.

Ensuite, créez un tableau de 5 éléments à l'aide de `Array.from()` et créez des composants `<Star>` individuels à l'aide de `Array.prototype.map()`. Gérez les événements `onMouseOver` et `onMouseLeave` de l'élément parent à l'aide de `hoverOver`. Gérez l'événement `onClick` à l'aide de `setRating`.

```css
.star {
  color: #ff9933;
  cursor: pointer;
}
```

```jsx
const Star = ({ marked, starId }) => {
  return (
    <span data-star-id={starId} className="star" role="button">
      {marked ? "\u2605" : "\u2606"}
    </span>
  );
};

const StarRating = ({ value }) => {
  const [rating, setRating] = React.useState(parseInt(value) || 0);
  const [selection, setSelection] = React.useState(0);

  const hoverOver = (event) => {
    let val = 0;
    if (event && event.target && event.target.getAttribute("data-star-id"))
      val = event.target.getAttribute("data-star-id");
    setSelection(val);
  };

  return (
    <div
      onMouseLeave={() => hoverOver(null)}
      onMouseOver={hoverOver}
      onClick={(e) =>
        setRating(e.target.getAttribute("data-star-id") || rating)
      }
    >
      {Array.from({ length: 5 }, (v, i) => (
        <Star
          starId={i + 1}
          key={`star_${i + 1}`}
          marked={selection ? selection >= i + 1 : rating >= i + 1}
        />
      ))}
    </div>
  );
};
```

Enfin, affichez le composant `StarRating` avec une valeur initiale de `2` en appelant `ReactDOM.createRoot(document.getElementById('root')).render(<StarRating value={2} />);`.

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
