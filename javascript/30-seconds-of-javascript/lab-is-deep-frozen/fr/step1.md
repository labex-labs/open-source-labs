# Comment vérifier si un objet est profondément congelé

Pour vérifier si un objet est profondément congelé, utilisez les étapes suivantes en JavaScript :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la récursion pour vérifier si toutes les propriétés de l'objet sont profondément congelées.
3. Utilisez `Object.isFrozen()` sur l'objet donné pour vérifier s'il est superficiquement congelé.
4. Utilisez `Object.keys()` pour obtenir toutes les propriétés de l'objet et `Array.prototype.every()` pour vérifier que toutes les clés sont soit des objets profondément congelés soit des valeurs non objets.

Voici un extrait de code d'exemple pour vérifier si un objet est profondément congelé :

```js
const isDeepFrozen = (obj) =>
  Object.isFrozen(obj) &&
  Object.keys(obj).every(
    (prop) => typeof obj[prop] !== "object" || isDeepFrozen(obj[prop])
  );
```

Vous pouvez utiliser la fonction `isDeepFrozen` pour vérifier si un objet est profondément congelé comme ceci :

```js
const x = Object.freeze({ a: 1 });
const y = Object.freeze({ b: { c: 2 } });
isDeepFrozen(x); // true
isDeepFrozen(y); // false
```
