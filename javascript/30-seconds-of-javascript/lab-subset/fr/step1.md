# Vérifier si un sous-ensemble d'un itérable est contenu dans un autre itérable

Pour pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`. Cette fonction vérifie si le premier itérable est un sous-ensemble du second itérable, en excluant les valeurs dupliquées.

Pour y arriver, vous pouvez faire ce qui suit :

- Créez un nouvel objet `Set` à partir de chaque itérable en utilisant le constructeur `Set`.
- Utilisez `Array.prototype.every()` et `Set.prototype.has()` pour vérifier si chaque valeur du premier itérable est contenue dans le second itérable.

Voici une implémentation exemple :

```js
const subSet = (a, b) => {
  const setA = new Set(a);
  const setB = new Set(b);
  return [...setA].every((value) => setB.has(value));
};
```

Vous pouvez utiliser la fonction `subSet` en passant deux ensembles à comparer. Par exemple :

```js
subSet(new Set([1, 2]), new Set([1, 2, 3, 4])); // true
subSet(new Set([1, 5]), new Set([1, 2, 3, 4])); // false
```
