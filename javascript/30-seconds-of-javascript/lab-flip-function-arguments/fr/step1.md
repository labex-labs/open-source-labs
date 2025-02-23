# Reorder Function Arguments with Flip

Pour inverser l'ordre des arguments d'une fonction, utilisez la fonction `flip`. Cette fonction prend une fonction en argument et renvoie une nouvelle fonction qui inverse le premier et le dernier argument.

Pour implémenter `flip` :

- Utilisez la déstructuration d'arguments et une fermeture avec des arguments variadiques.
- Utilisez l'opérateur de propagation (`...`) pour insérer le premier argument en dernier avant d'appliquer le reste.

```js
const flip =
  (fn) =>
  (first, ...rest) =>
    fn(...rest, first);
```

Voici un exemple de l'utilisation de `flip` pour inverser les arguments de `Object.assign` :

```js
let a = { name: "John Smith" };
let b = {};

// Crée une nouvelle fonction qui inverse les arguments de Object.assign
const mergeFrom = flip(Object.assign);

// Crée une nouvelle fonction qui lie le premier argument à a
let mergePerson = mergeFrom.bind(null, a);

// Appelle la nouvelle fonction avec b comme deuxième argument
mergePerson(b); // b est maintenant égal à a

// Alternativement, fusionnez a et b sans utiliser la nouvelle fonction
b = {};
Object.assign(b, a); // b est maintenant égal à a
```
