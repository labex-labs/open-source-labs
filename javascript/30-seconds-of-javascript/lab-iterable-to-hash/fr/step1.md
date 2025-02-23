# Conversion d'un itérable en un hachage

Pour convertir un itérable (objet ou tableau) en un hachage (magasin de données indexé), suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Object.values()` pour obtenir les valeurs de l'itérable.
3. Utilisez `Array.prototype.reduce()` pour itérer sur les valeurs et créer un objet qui est indexé par la valeur de référence.
4. Appelez la fonction `toHash` avec l'itérable et un paramètre clé optionnel pour spécifier la valeur de référence.

Voici une implémentation de l'exemple de la fonction `toHash` en JavaScript :

```js
const toHash = (iterable, key) =>
  Object.values(iterable).reduce((acc, data, index) => {
    acc[!key ? index : data[key]] = data;
    return acc;
  }, {});
```

Vous pouvez appeler la fonction `toHash` avec différents itérables et clés pour créer différents hachages. Par exemple :

```js
toHash([4, 3, 2, 1]); // { 0: 4, 1: 3, 2: 2, 3: 1 }
toHash([{ a: "label" }], "a"); // { label: { a: 'label' } }
```
