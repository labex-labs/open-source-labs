# Fonction pour formater les secondes au format ISO

Pour utiliser ce code, ouvrez le Terminal/SSH et tapez `node`. Cette fonction prend un nombre de secondes en argument et renvoie le format de temps ISO. Voici comment elle fonctionne :

- Divisez le nombre de secondes par les valeurs appropriées pour obtenir les valeurs correspondantes pour `heure`, `minute` et `seconde`.
- Stockez le signe du nombre dans une variable pour l'ajouter au début du résultat.
- Utilisez `Array.prototype.map()` en combinaison avec `Math.floor()` et `String.prototype.padStart()` pour convertir en chaîne de caractères et formater chaque segment.
- Utilisez `Array.prototype.join()` pour combiner les valeurs en une chaîne de caractères.

Voici le code :

```js
const formatSeconds = (s) => {
  const [hour, minute, second, sign] =
    s > 0
      ? [s / 3600, (s / 60) % 60, s % 60, ""]
      : [-s / 3600, (-s / 60) % 60, -s % 60, "-"];

  return (
    sign +
    [hour, minute, second]
      .map((v) => `${Math.floor(v)}`.padStart(2, "0"))
      .join(":")
  );
};
```

Vous pouvez tester la fonction avec ces exemples :

```js
formatSeconds(200); // '00:03:20'
formatSeconds(-200); // '-00:03:20'
formatSeconds(99999); // '27:46:39'
```
