# React useNavigatorOnLine Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Pour vérifier si le client est en ligne ou hors ligne, vous pouvez créer une fonction `getOnLineStatus` qui utilise l'API web `Navigator.onLine`. Ensuite, pour implémenter cette fonctionnalité dans un composant React, vous pouvez utiliser le hook personnalisé `useNavigatorOnLine`. Ce hook crée une variable d'état appelée `status` à l'aide du hook `useState()` et la définit sur la valeur renvoyée par `getOnLineStatus()`. Le hook `useEffect()` est utilisé pour ajouter des écouteurs d'événements pour le changement d'état en ligne/hors ligne, mettre à jour la variable d'état `status` en conséquence et nettoyer ces écouteurs lorsque le composant est démonté. Enfin, la variable `isOnline` renvoyée par `useNavigatorOnLine()` peut être utilisée pour afficher un message indiquant si le client est en ligne ou hors ligne.

```jsx
const getOnLineStatus = () =>
  typeof navigator !== "undefined" && typeof navigator.onLine === "boolean"
    ? navigator.onLine
    : true;

const useNavigatorOnLine = () => {
  const [status, setStatus] = React.useState(getOnLineStatus());

  const setOnline = () => setStatus(true);
  const setOffline = () => setStatus(false);

  React.useEffect(() => {
    window.addEventListener("online", setOnline);
    window.addEventListener("offline", setOffline);

    return () => {
      window.removeEventListener("online", setOnline);
      window.removeEventListener("offline", setOffline);
    };
  }, []);

  return status;
};

const StatusIndicator = () => {
  const isOnline = useNavigatorOnLine();

  return <span>You are {isOnline ? "online" : "offline"}.</span>;
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <StatusIndicator />
);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
