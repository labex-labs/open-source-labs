# Comment retarder l'exécution d'une fonction asynchrone en JavaScript

Pour retarder l'exécution d'une fonction asynchrone en JavaScript, vous pouvez utiliser la fonction `sleep` ci-dessous, qui renvoie une `Promise` qui se résout après un certain temps. Voici un exemple de retard de l'exécution d'une partie d'une fonction `async` à l'aide de `sleep` :

```js
const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

async function sleepyWork() {
  console.log("Je vais dormir pendant 1 seconde.");
  await sleep(1000);
  console.log("Je me suis réveillé après 1 seconde.");
}
```

Pour utiliser cette fonction, appelez simplement `sleepyWork()` et la console affichera les messages avec un retard de 1 seconde entre eux.
