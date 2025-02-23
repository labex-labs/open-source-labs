# Comment déterminer si l'environnement d'exécution actuel est Node.js

Pour déterminer si l'environnement d'exécution actuel est Node.js, suivez ces étapes :

1. Ouvrez le Terminal/SSH.
2. Tapez `node`.
3. Utilisez l'objet global `process` qui fournit des informations sur le processus Node.js actuel.
4. Vérifiez si `process`, `process.versions` et `process.versions.node` sont définis.

Voici le code pour déterminer si l'environnement d'exécution actuel est Node.js :

```js
const isNode = () =>
  typeof process !== "undefined" &&
  !!process.versions &&
  !!process.versions.node;
```

Vous pouvez tester le code en appelant la fonction `isNode` :

```js
isNode(); // true (Node)
isNode(); // false (navigateur)
```
