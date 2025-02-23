# Mesurer le temps pris par une fonction

Pour mesurer le temps pris par une fonction, utilisez `console.time()` et `console.timeEnd()` pour déterminer la différence entre les temps de début et de fin.

Voici un exemple de fonction appelée `timeTaken` qui mesure le temps pris par une fonction de rappel :

```js
const timeTaken = (callback) => {
  console.time("timeTaken");
  const result = callback();
  console.timeEnd("timeTaken");
  return result;
};
```

Pour utiliser cette fonction, passez simplement votre fonction de rappel en argument. Par exemple :

```js
timeTaken(() => Math.pow(2, 10)); // Retourne 1024, et affiche dans la console : timeTaken: 0.02099609375ms
```

Dans l'exemple ci-dessus, la fonction `timeTaken` est utilisée pour mesurer le temps pris pour exécuter l'appel de fonction `Math.pow(2, 10)`, qui retourne 1024. La sortie de la console montrera le temps pris en millisecondes (ms).
