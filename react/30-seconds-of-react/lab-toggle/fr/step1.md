# Toggle

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Pour afficher un composant bascule, suivez ces étapes :

1. Utilisez le hook `useState()` pour initialiser la variable d'état `isToggledOn` à `defaultToggled`.
2. Affichez un élément `<input>` et liez son événement `onClick` pour mettre à jour la variable d'état `isToggledOn`. Appliquez la `className` appropriée à l'élément `<label>` d'enveloppement.
3. Utilisez le CSS suivant pour styliser le composant bascule :

```css
.toggle input[type="checkbox"] {
  display: none;
}

.toggle.on {
  background-color: green;
}

.toggle.off {
  background-color: red;
}
```

Voici le code :

```jsx
const Toggle = ({ defaultToggled = false }) => {
  const [isToggleOn, setIsToggleOn] = React.useState(defaultToggled);

  return (
    <label className={isToggleOn ? "toggle on" : "toggle off"}>
      <input
        type="checkbox"
        checked={isToggleOn}
        onChange={() => setIsToggleOn(!isToggleOn)}
      />
      {isToggleOn ? "ON" : "OFF"}
    </label>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Toggle />);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
