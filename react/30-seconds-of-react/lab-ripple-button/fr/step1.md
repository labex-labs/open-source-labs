# Bouton avec effet d'onde (Ripple Effect)

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle (VM). En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Ce code affiche un composant bouton qui crée un effet d'onde lorsqu'il est cliqué. Voici comment cela fonctionne :

- Le hook `useState()` est utilisé pour créer deux variables d'état : `coords` et `isRippling`. La variable `coords` stocke les coordonnées du pointeur, tandis que `isRippling` stocke l'état d'animation du bouton.
- Un hook `useEffect()` est utilisé pour changer la valeur de `isRippling` chaque fois que la variable d'état `coords` change. Cela lance l'animation de l'effet d'onde.
- `setTimeout()` est utilisé dans le hook précédent pour effacer l'animation une fois qu'elle a terminé de jouer.
- Un autre hook `useEffect()` est utilisé pour réinitialiser `coords` chaque fois que la variable d'état `isRippling` est `false`.
- L'événement `onClick` est géré en mettant à jour la variable d'état `coords` et en appelant la fonction de rappel (callback) passée.

Voici le code pour le composant `RippleButton` :

```jsx
const RippleButton = ({ children, onClick }) => {
  const [coords, setCoords] = React.useState({ x: -1, y: -1 });
  const [isRippling, setIsRippling] = React.useState(false);

  React.useEffect(() => {
    if (coords.x !== -1 && coords.y !== -1) {
      setIsRippling(true);
      setTimeout(() => setIsRippling(false), 300);
    } else setIsRippling(false);
  }, [coords]);

  React.useEffect(() => {
    if (!isRippling) setCoords({ x: -1, y: -1 });
  }, [isRippling]);

  return (
    <button
      className="ripple-button"
      onClick={(e) => {
        const rect = e.target.getBoundingClientRect();
        setCoords({ x: e.clientX - rect.left, y: e.clientY - rect.top });
        onClick && onClick(e);
      }}
    >
      {isRippling && (
        <span
          className="ripple"
          style={{
            left: coords.x,
            top: coords.y
          }}
        />
      )}
      <span className="content">{children}</span>
    </button>
  );
};
```

Vous pouvez utiliser ce composant comme ceci :

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <RippleButton onClick={(e) => console.log(e)}>Click me</RippleButton>
);
```

Et voici le CSS pour le composant `RippleButton` :

```css
.ripple-button {
  border-radius: 4px;
  border: none;
  margin: 8px;
  padding: 14px 24px;
  background: #1976d2;
  color: #fff;
  overflow: hidden;
  position: relative;
  cursor: pointer;
}

.ripple-button > .ripple {
  width: 20px;
  height: 20px;
  position: absolute;
  background: #63a4ff;
  display: block;
  content: "";
  border-radius: 9999px;
  opacity: 1;
  animation: 0.9s ease 1 forwards ripple-effect;
}

@keyframes ripple-effect {
  0% {
    transform: scale(1);
    opacity: 1;
  }
  50% {
    transform: scale(10);
    opacity: 0.375;
  }
  100% {
    transform: scale(35);
    opacity: 0;
  }
}

.ripple-button > .content {
  position: relative;
  z-index: 2;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
