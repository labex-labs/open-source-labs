# Instructions pour cloner profondément un objet

Pour cloner profondément un objet, suivez ces étapes :

1. Créez une nouvelle instance de terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la récursivité pour cloner des primitifs, des tableaux et des objets, en excluant les instances de classe.
3. Vérifiez si l'objet passé est `null` et, si c'est le cas, renvoyez `null`.
4. Utilisez `Object.assign()` et un objet vide (`{}`) pour créer un clonage superficiel de l'original.
5. Utilisez `Object.keys()` et `Array.prototype.forEach()` pour déterminer quelles paires clé-valeur doivent être clonées profondément.
6. Si l'objet est un `Array`, définissez la `length` du `clone` sur celle de l'original et utilisez `Array.from()` pour créer un clone.
7. Utilisez le code suivant pour implémenter le clonage profond :

```js
const deepClone = (obj) => {
  if (obj === null) return null;
  let clone = Object.assign({}, obj);
  Object.keys(clone).forEach(
    (key) =>
      (clone[key] =
        typeof obj[key] === "object" ? deepClone(obj[key]) : obj[key])
  );
  if (Array.isArray(obj)) {
    clone.length = obj.length;
    return Array.from(clone);
  }
  return clone;
};
```

Utilisez le code suivant pour tester votre fonction de clonage profond :

```js
const a = { foo: "bar", obj: { a: 1, b: 2 } };
const b = deepClone(a); // a!== b, a.obj!== b.obj
```
