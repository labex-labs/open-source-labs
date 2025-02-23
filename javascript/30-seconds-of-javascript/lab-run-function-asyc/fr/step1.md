# Exécution de fonction asynchrone à l'aide de Web Workers

Pour exécuter une fonction sans bloquer l'interface utilisateur, utilisez un Web Worker pour exécuter la fonction dans un fil séparé. Voici comment :

1. Créez un `Worker` à l'aide d'une URL d'objet `Blob`, avec le contenu étant la version sérialisée de la fonction à exécuter.
2. Affichez immédiatement la valeur de retour de l'appel de la fonction.
3. Retournez une `Promise`, en écoutant les événements `onmessage` et `onerror` et en résolvant les données envoyées en retour par le worker, ou en lançant une erreur.

```js
const runAsync = (fn) => {
  const worker = new Worker(
    URL.createObjectURL(new Blob([`postMessage((${fn})());`]), {
      type: "application/javascript; charset=utf-8"
    })
  );
  return new Promise((resolve, reject) => {
    worker.onmessage = ({ data }) => {
      resolve(data);
      worker.terminate();
    };
    worker.onerror = (error) => {
      reject(error);
      worker.terminate();
    };
  });
};
```

Notez que la fonction fournie à `runAsync` ne devrait pas utiliser de closures car tout est sérialisé et devient littéral. Par conséquent, toutes les variables et les fonctions doivent être définies à l'intérieur. Voici quelques exemples :

```js
const longRunningFunction = () => {
  let result = 0;
  for (let i = 0; i < 1000; i++)
    for (let j = 0; j < 700; j++)
      for (let k = 0; k < 300; k++) result = result + i + j + k;

  return result;
};

runAsync(longRunningFunction).then(console.log); // 209685000000
runAsync(() => 10 ** 3).then(console.log); // 1000
let outsideVariable = 50;
runAsync(() => typeof outsideVariable).then(console.log); // 'undefined'
```
