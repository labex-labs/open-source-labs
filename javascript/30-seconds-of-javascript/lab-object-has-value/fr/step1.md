# Fonction pour Vérifier si un Objet Contient une Valeur Spécifique

Pour vérifier si un objet contient une valeur spécifique, utilisez la fonction suivante :

```js
const hasValue = (obj, value) => Object.values(obj).includes(value);
```

Pour utiliser cette fonction, passez l'objet que vous voulez rechercher et la valeur cible en arguments. La fonction renverra `true` si l'objet contient la valeur et `false` s'il ne la contient pas.

Voici un exemple :

```js
const obj = { a: 100, b: 200 };
console.log(hasValue(obj, 100)); // true
console.log(hasValue(obj, 999)); // false
```

Pour commencer à coder, ouvrez le Terminal/SSH et tapez `node`.
