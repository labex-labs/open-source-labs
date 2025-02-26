# Minuteur à rebours

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Ce code crée un minuteur à rebours qui affiche un message lorsqu'il atteint zéro. Pour le mettre en œuvre, les étapes suivantes sont suivies :

1. Utilisez le hook `useState()` pour créer une variable d'état `time` qui stocke la valeur du temps. Initialisez-la à partir des props et déstructurez-la en ses composants.
2. Utilisez le hook `useState()` pour créer les variables d'état `paused` et `over`, qui sont utilisées pour empêcher le minuteur de compter si il est en pause ou si le temps est écoulé.
3. Créez une méthode `tick` qui met à jour les valeurs du temps en fonction de la valeur actuelle (c'est-à-dire en diminuant le temps d'une seconde).
4. Créez une méthode `reset` qui remet toutes les variables d'état à leurs états initiaux.
5. Utilisez le hook `useEffect()` pour appeler la méthode `tick` toutes les secondes via l'utilisation de `setInterval()` et utilisez `clearInterval()` pour nettoyer lorsque le composant est démonté.
6. Utilisez `String.prototype.padStart()` pour ajouter des zéros devant chaque partie du tableau de temps pour créer la représentation visuelle du minuteur.

```jsx
const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
  const [paused, setPaused] = React.useState(false);
  const [over, setOver] = React.useState(false);
  const [[h, m, s], setTime] = React.useState([hours, minutes, seconds]);

  const tick = () => {
    if (paused || over) return;
    if (h === 0 && m === 0 && s === 0) setOver(true);
    else if (m === 0 && s === 0) setTime([h - 1, 59, 59]);
    else if (s == 0) setTime([h, m - 1, 59]);
    else setTime([h, m, s - 1]);
  };

  const reset = () => {
    setTime([parseInt(hours), parseInt(minutes), parseInt(seconds)]);
    setPaused(false);
    setOver(false);
  };

  React.useEffect(() => {
    const timerID = setInterval(tick, 1000);
    return () => clearInterval(timerID);
  });

  return (
    <div>
      <p>
        {`${h.toString().padStart(2, "0")}:${m.toString().padStart(2, "0")}:${s
          .toString()
          .padStart(2, "0")}`}
      </p>
      {over && <div>Le temps est écoulé!</div>}
      <button onClick={() => setPaused(!paused)}>
        {paused ? "Reprendre" : "Pause"}
      </button>
      <button onClick={reset}>Redémarrer</button>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <CountDown hours={1} minutes={45} />
);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
