# Chaining Asynchronous Functions

Pour chaîner des fonctions asynchrones, ouvrez le Terminal/SSH et tapez `node`. Ensuite, parcourez un tableau de fonctions contenant des événements asynchrones et appelez la fonction `next` lorsque chaque événement asynchrone est terminé.

Voici un extrait de code qui montre comment chaîner des fonctions asynchrones :

```js
const chainAsync = (fns) => {
  let curr = 0;
  const last = fns[fns.length - 1];
  const next = () => {
    const fn = fns[curr++];
    fn === last ? fn() : fn(next);
  };
  next();
};

chainAsync([
  (next) => {
    console.log("0 seconds");
    setTimeout(next, 1000);
  },
  (next) => {
    console.log("1 second");
    setTimeout(next, 1000);
  },
  () => {
    console.log("2 second");
  }
]);
```
