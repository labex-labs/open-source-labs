# Algorithme de tri bulle

Pour pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node` pour démarrer. L'algorithme de tri bulle trie un tableau de nombres.

Étapes pour trier un tableau en utilisant l'algorithme de tri bulle :

1. Décarez une variable, `swapped`, qui indique si des valeurs ont été échangées lors de l'itération actuelle.

2. Utilisez l'opérateur de répandage (`...`) pour cloner le tableau original, `arr`.

3. Utilisez une boucle `for` pour itérer sur les éléments du tableau cloné, en terminant avant le dernier élément.

4. Utilisez une boucle `for` imbriquée pour itérer sur le segment du tableau entre `0` et `i`, en échangeant tout élément adjacent non trié et en mettant `swapped` à `true`.

5. Si `swapped` est `false` après une itération, plus de modifications ne sont nécessaires, donc le tableau cloné est renvoyé.

Exemple de code :

```js
const bubbleSort = (arr) => {
  let swapped = false;
  const a = [...arr];
  for (let i = 1; i < a.length; i++) {
    swapped = false;
    for (let j = 0; j < a.length - i; j++) {
      if (a[j + 1] < a[j]) {
        [a[j], a[j + 1]] = [a[j + 1], a[j]];
        swapped = true;
      }
    }
    if (!swapped) return a;
  }
  return a;
};

bubbleSort([2, 1, 4, 3]); // [1, 2, 3, 4]
```
