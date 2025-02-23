# Comment sérialiser un JSON circulaire

Pour sérialiser un objet JSON qui contient des références circulaires, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Créez un `WeakSet` pour stocker et vérifier les valeurs déjà vues en utilisant `WeakSet.prototype.add()` et `WeakSet.prototype.has()`.
3. Utilisez `JSON.stringify()` avec une fonction de remplacement personnalisée qui ignore les valeurs déjà présentes dans `seen` et ajoute de nouvelles valeurs si nécessaire.
4. ⚠️ **ATTENTION** : Cette fonction trouve et supprime les références circulaires, ce qui entraîne une perte de données circulaires dans le JSON sérialisé.

Voici le code de la fonction `stringifyCircularJSON` :

```js
const stringifyCircularJSON = (obj) => {
  const seen = new WeakSet();
  return JSON.stringify(obj, (key, value) => {
    if (value !== null && typeof value === "object") {
      if (seen.has(value)) return;
      seen.add(value);
    }
    return value;
  });
};
```

Pour tester la fonction, vous pouvez créer un objet avec une référence circulaire et appeler `stringifyCircularJSON` :

```js
const obj = { n: 42 };
obj.obj = obj;
stringifyCircularJSON(obj); // '{"n": 42}'
```
