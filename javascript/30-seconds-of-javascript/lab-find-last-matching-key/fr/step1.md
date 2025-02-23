# Fonction pour Trouver la Dernière Clé qui Correspond à une Condition

Pour trouver la dernière clé dans un objet qui satisfait une condition donnée, utilisez la fonction `findLastKey`. Cette fonction prend un objet et une fonction de test comme arguments. Si une clé correspondante est trouvée, la fonction la renvoie. Sinon, elle renvoie `undefined`. Voici les étapes que la fonction utilise pour trouver la dernière clé :

1. Utilisez `Object.keys()` pour obtenir toutes les propriétés de l'objet.
2. Utilisez `Array.prototype.reverse()` pour inverser l'ordre des clés.
3. Utilisez `Array.prototype.find()` pour tester la fonction fournie pour chaque paire clé-valeur. La fonction de rappel reçoit trois arguments - la valeur, la clé et l'objet.
4. Si une clé correspondante est trouvée, renvoyez-la.

```js
const findLastKey = (obj, fn) =>
  Object.keys(obj)
    .reverse()
    .find((key) => fn(obj[key], key, obj));
```

Voici un exemple d'utilisation de `findLastKey` :

```js
findLastKey(
  {
    barney: { age: 36, active: true },
    fred: { age: 40, active: false },
    pebbles: { age: 1, active: true }
  },
  (x) => x["active"]
); // 'pebbles'
```

Pour utiliser cette fonction, ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
