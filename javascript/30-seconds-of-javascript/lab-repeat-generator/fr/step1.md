# Entraînement au code avec le générateur de répétition

Pour vous entraîner au codage, ouvrez le Terminal/SSH et tapez `node` pour créer un générateur qui répète indéfiniment la valeur donnée. Utilisez une boucle `while` non terminante qui `yield` une valeur chaque fois que `Generator.prototype.next()` est appelée. Ensuite, utilisez la valeur de retour de l'instruction `yield` pour mettre à jour la valeur retournée si la valeur passée n'est pas `undefined`.

```js
const repeatGenerator = function* (val) {
  let v = val;
  while (true) {
    let newV = yield v;
    if (newV !== undefined) v = newV;
  }
};
```

Pour tester le générateur, créez une instance de celui-ci en utilisant la valeur `5` et appelez `repeater.next()` pour obtenir la prochaine valeur de la séquence. La sortie sera `{ value: 5, done: false }`. Appeler `repeater.next()` à nouveau renverra la même valeur. Pour changer la valeur, appelez `repeater.next(4)`, qui renverra `{ value: 4, done: false }`. Enfin, appeler `repeater.next()` renverra la valeur mise à jour, `{ value: 4, done: false }`.
