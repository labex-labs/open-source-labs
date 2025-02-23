# Comment obtenir une valeur imbriquée dans un objet JSON

Pour extraire une valeur cible d'un objet JSON imbriqué sur la base d'une clé donnée, suivez ces étapes :

- Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
- Vérifiez si la `cible` existe dans l'`obj` en utilisant l'opérateur `in`.
- Si la `cible` est trouvée, renvoyez la valeur correspondante dans l'`obj`.
- Si la `cible` n'est pas trouvée, utilisez `Object.values()` et `Array.prototype.reduce()` pour appeler récursivement la fonction `dig` sur chaque objet imbriqué jusqu'à ce que la première paire clé/valeur correspondante soit trouvée.

Voici le code de la fonction `dig` :

```js
const dig = (obj, target) =>
  target in obj
    ? obj[target]
    : Object.values(obj).reduce((acc, val) => {
        if (acc !== undefined) return acc;
        if (typeof val === "object") return dig(val, target);
      }, undefined);
```

Pour utiliser la fonction `dig`, créez d'abord un objet JSON avec des niveaux imbriqués, comme ceci :

```js
const data = {
  niveau1: {
    niveau2: {
      niveau3: "quelques données"
    }
  }
};
```

Ensuite, appelez la fonction `dig` avec l'objet JSON et la clé souhaitée :

```js
dig(data, "niveau3"); // 'quelques données'
dig(data, "niveau4"); // undefined
```

Ces exemples renverront la valeur de la clé `niveau3` dans l'objet `data` et `undefined` pour la clé inexistante `niveau4`.
