# Conversion de la sortie d'un générateur en tableau

Pour convertir la sortie d'une fonction génératrice en tableau, utilisez l'opérateur de propagation (`...`). Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.

Voici une fonction d'exemple qui convertit un générateur en tableau :

```js
const generatorToArray = (gen) => [...gen];
```

Vous pouvez utiliser cette fonction comme suit :

```js
const s = new Set([1, 2, 1, 3, 1, 4]);
generatorToArray(s.entries()); // [[ 1, 1 ], [ 2, 2 ], [ 3, 3 ], [ 4, 4 ]]
```
