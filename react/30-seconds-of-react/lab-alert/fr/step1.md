# Alerte fermable (Closable Alert)

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle (VM). En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Rend un composant d'alerte avec la prop `type`.

Le composant `Alert` prend les props suivantes :

- `isDefaultShown` : un booléen qui détermine si l'alerte est affichée initialement ou non (la valeur par défaut est `false`)
- `timeout` : un nombre qui spécifie la durée en millisecondes avant que l'alerte ne disparaisse progressivement (la valeur par défaut est `250`)
- `type` : une chaîne de caractères qui détermine le type d'alerte (par exemple, "warning", "error", "info")
- `message` : une chaîne de caractères qui contient le message à afficher dans l'alerte

Le composant effectue les actions suivantes :

- Utilise le hook `useState()` pour créer les variables d'état `isShown` et `isLeaving` et les initialise toutes les deux à `false`.
- Définit une variable `timeoutId` pour conserver l'instance du minuteur afin de l'annuler lorsque le composant est démonté.
- Utilise le hook `useEffect()` pour mettre à jour la valeur de `isShown` à `true` et annuler l'intervalle en utilisant `timeoutId` lorsque le composant est démonté.
- Définit une fonction `closeAlert` pour marquer le composant comme supprimé du DOM en affichant une animation de disparition progressive et en définissant `isShown` à `false` via `setTimeout()`.
- Rend le composant d'alerte si `isShown` est `true`. Le composant a les styles appropriés en fonction de la prop `type` et disparaît progressivement si `isLeaving` est `true`.

Voici le code :

```css
@keyframes leave {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}

.alert {
  padding: 0.75rem 0.5rem;
  margin-bottom: 0.5rem;
  text-align: left;
  padding-right: 40px;
  border-radius: 4px;
  font-size: 16px;
  position: relative;
}

.alert.warning {
  color: #856404;
  background-color: #fff3cd;
  border-color: #ffeeba;
}

.alert.error {
  color: #721c24;
  background-color: #f8d7da;
  border-color: #f5c6cb;
}

.alert.leaving {
  animation: leave 0.5s forwards;
}

.alert.close {
  position: absolute;
  top: 0;
  right: 0;
  padding: 0 0.75rem;
  color: #333;
  border: 0;
  height: 100%;
  cursor: pointer;
  background: none;
  font-weight: 600;
  font-size: 16px;
}

.alert.close::after {
  content: "x";
}
```

```jsx
const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
  const [isShown, setIsShown] = React.useState(isDefaultShown);
  const [isLeaving, setIsLeaving] = React.useState(false);

  let timeoutId = null;

  React.useEffect(() => {
    setIsShown(true);
    return () => {
      clearTimeout(timeoutId);
    };
  }, [isDefaultShown, timeout, timeoutId]);

  const closeAlert = () => {
    setIsLeaving(true);
    timeoutId = setTimeout(() => {
      setIsLeaving(false);
      setIsShown(false);
    }, timeout);
  };

  return (
    isShown && (
      <div
        className={`alert ${type} ${isLeaving ? "leaving" : ""}`}
        role="alert"
      >
        <button className="close" onClick={closeAlert} />
        {message}
      </div>
    )
  );
};
```

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Alert type="info" message="This is info" />
);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
