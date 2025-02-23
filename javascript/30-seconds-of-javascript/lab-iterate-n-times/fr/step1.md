# Code Practice: Iterating N Times

Pour pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`. Une fois que vous avez fait cela, utilisez la fonction suivante pour itérer sur une fonction de rappel `n` fois :

```js
const times = (n, fn, context = undefined) => {
  let i = 0;
  while (fn.call(context, i) !== false && ++i < n) {}
};
```

Pour utiliser cette fonction, appelez `times()` et passez les arguments suivants :

- `n` : le nombre de fois que vous voulez itérer sur la fonction de rappel
- `fn` : la fonction de rappel sur laquelle vous voulez itérer
- `context` (optionnel) : le contexte que vous voulez utiliser pour la fonction de rappel (si non spécifié, il utilisera un objet `undefined` ou l'objet global en mode non strict)

Voici un exemple d'utilisation de la fonction `times()` :

```js
var output = "";
times(5, (i) => (output += i));
console.log(output); // 01234
```

Cela itérera sur la fonction de rappel `i => (output += i)` 5 fois et stockera la sortie dans la variable `output`. La sortie sera ensuite affichée dans la console, qui affichera `01234`.
