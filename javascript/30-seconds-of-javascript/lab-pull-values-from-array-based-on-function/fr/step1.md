# Comment extraire des valeurs d'un tableau en fonction d'une fonction donnée

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.

La fonction `pullBy` modifie le tableau original en filtrant les valeurs spécifiées en fonction d'une fonction itératrice donnée. Voici comment elle fonctionne :

1. Vérifiez si le dernier argument fourni est une fonction.
2. Utilisez `Array.prototype.map()` pour appliquer la fonction itératrice `fn` à tous les éléments du tableau.
3. Utilisez `Array.prototype.filter()` et `Array.prototype.includes()` pour extraire les valeurs qui ne sont pas nécessaires.
4. Définissez `Array.prototype.length` pour réinitialiser la longueur du tableau passé en paramètre à `0`.
5. Utilisez `Array.prototype.push()` pour le remplir uniquement avec les valeurs extraites.

Voici le code :

```js
const pullBy = (arr, ...args) => {
  const length = args.length;
  let fn = length > 1 ? args[length - 1] : undefined;
  fn = typeof fn == "function" ? (args.pop(), fn) : undefined;
  let argState = (Array.isArray(args[0]) ? args[0] : args).map((val) =>
    fn(val)
  );
  let pulled = arr.filter((v, i) => !argState.includes(fn(v)));
  arr.length = 0;
  pulled.forEach((v) => arr.push(v));
};
```

Et voici un exemple de son utilisation :

```js
var myArray = [{ x: 1 }, { x: 2 }, { x: 3 }, { x: 1 }];
pullBy(myArray, [{ x: 1 }, { x: 3 }], (o) => o.x); // myArray = [{ x: 2 }]
```

Notez que dans cet exemple, nous extrayons tous les éléments ayant une propriété `x` égale à `1` ou `3`. Le `myArray` résultant ne contiendra que l'élément ayant une propriété `x` égale à `2`.
