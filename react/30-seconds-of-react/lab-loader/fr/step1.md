# Chargeur tournant

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

**Affiche un composant de chargeur tournant.**

Pour afficher un composant de chargeur tournant, suivez ces étapes :

1. Affichez un élément SVG dont les dimensions sont déterminées par la propriété `size`.
2. Utilisez CSS pour animer l'SVG, créant une animation de rotation. Plus précisément, ajoutez la classe `.loader` à l'SVG et définissez la propriété `animation` sur `rotate 2s linear infinite`. Définissez également les clés `rotate` avec une propriété `transform` qui fait tourner l'SVG de 360 degrés.
3. Ajoutez un élément `circle` à l'SVG, qui représente le cercle tournant. Pour animer le cercle, ajoutez le sélecteur `.loader circle` et définissez la propriété `animation` sur `dash 1.5s ease-in-out infinite`. Définissez également les clés `dash` avec les propriétés `stroke-dasharray` et `stroke-dashoffset` qui créent un motif de trait pointillé qui se déplace autour du cercle.
4. Enfin, créez un composant `Loader` qui affiche l'SVG avec la propriété `size` passée en tant qu'attributs de largeur et de hauteur.

```css
.loader {
  animation: rotate 2s linear infinite;
}

@keyframes rotate {
  100% {
    transform: rotate(360deg);
  }
}

.loader circle {
  animation: dash 1.5s ease-in-out infinite;
}

@keyframes dash {
  0% {
    stroke-dasharray: 1, 150;
    stroke-dashoffset: 0;
  }
  50% {
    stroke-dasharray: 90, 150;
    stroke-dashoffset: -35;
  }
  100% {
    stroke-dasharray: 90, 150;
    stroke-dashoffset: -124;
  }
}
```

```jsx
const Loader = ({ size }) => {
  return (
    <svg
      className="loader"
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <circle cx="12" cy="12" r="10" />
    </svg>
  );
};
```

Pour utiliser le composant `Loader` avec une taille de 24, appelez `ReactDOM.createRoot(document.getElementById('root')).render(<Loader size={24} />);`.

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
