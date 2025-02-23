# Conversion d'un objet en un tableau de paires clé-valeur

Pour convertir un objet en un tableau de paires clé-valeur, vous pouvez suivre les étapes suivantes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la méthode `Object.entries()` pour obtenir un tableau d'éléments de type tableau de paires clé-valeur à partir de l'objet.
3. Créez une fonction appelée `objectToPairs` qui accepte un objet en argument et renvoie le tableau de paires clé-valeur.
4. Appelez la fonction `objectToPairs` avec un objet d'exemple pour tester la sortie.

Voici une implémentation d'exemple :

```js
const objectToPairs = (obj) => Object.entries(obj);
objectToPairs({ a: 1, b: 2 }); // [ ['a', 1], ['b', 2] ]
```

En suivant ces étapes, vous pouvez facilement convertir un objet en un tableau de paires clé-valeur à l'aide de JavaScript.
