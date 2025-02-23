# Voici comment trouver la somme d'un tableau

Pour trouver la somme d'un tableau de nombres, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à coder.
2. Utilisez la méthode `Array.prototype.reduce()` pour ajouter chaque valeur à un accumulateur, qui doit être initialisé avec une valeur de `0`.
3. Voici le code que vous pouvez utiliser pour trouver la somme du tableau :

```js
const sum = (...arr) => [...arr].reduce((acc, val) => acc + val, 0);
```

4. Pour tester la fonction `sum`, utilisez les exemples de code suivants :

```js
sum(1, 2, 3, 4); // 10
sum(...[1, 2, 3, 4]); // 10
```

En suivant ces étapes, vous pouvez facilement trouver la somme d'un tableau de nombres à l'aide de JavaScript.
