# Fonction JavaScript pour Vérifier si un Objet a une Clé

Pour vérifier si une valeur cible existe dans un objet JavaScript, utilisez la fonction `hasKey`.

La fonction prend deux arguments : `obj`, l'objet JSON dans lequel chercher, et `keys`, un tableau de clés à vérifier. Voici les étapes pour vérifier si l'objet a la clé (ou les clés) donnée(s) :

1. Vérifiez si le tableau `keys` n'est pas vide. Si c'est le cas, renvoyez `false`.
2. Utilisez la méthode `Array.prototype.every()` pour itérer sur le tableau `keys` et vérifier séquentiellement chaque clé jusqu'à la profondeur interne de `obj`.
3. Utilisez la méthode `Object.prototype.hasOwnProperty()` pour vérifier si `obj` n'a pas la clé actuelle ou n'est pas un objet. Si l'une de ces conditions est vraie, arrêtez la propagation et renvoyez `false`.
4. Sinon, affectez la valeur de la clé à `obj` pour l'utiliser dans l'itération suivante.
5. Si le tableau `keys` a été entièrement itéré avec succès, renvoyez `true`.

Voici le code pour la fonction `hasKey` :

```js
const hasKey = (obj, keys) => {
  return (
    keys.length > 0 &&
    keys.every((key) => {
      if (typeof obj !== "object" || !obj.hasOwnProperty(key)) return false;
      obj = obj[key];
      return true;
    })
  );
};
```

Voici quelques exemples d'utilisation de la fonction `hasKey` :

```js
let obj = {
  a: 1,
  b: { c: 4 },
  "b.d": 5
};

hasKey(obj, ["a"]); // true
hasKey(obj, ["b"]); // true
hasKey(obj, ["b", "c"]); // true
hasKey(obj, ["b.d"]); // true
hasKey(obj, ["d"]); // false
hasKey(obj, ["c"]); // false
hasKey(obj, ["b", "f"]); // false
```
