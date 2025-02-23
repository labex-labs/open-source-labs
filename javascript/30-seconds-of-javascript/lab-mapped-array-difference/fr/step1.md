# Fonction pour retourner la différence de deux tableaux en utilisant la mise en correspondance

Pour commencer à coder, ouvrez votre Terminal/SSH et tapez `node`.

Cette fonction prend deux tableaux et applique la fonction fournie à chaque élément des deux tableaux pour retourner leur différence.

Pour ce faire :

- Créez un `Set` en appliquant la fonction (`fn`) à chaque élément du second tableau (`b`).
- Utilisez `Array.prototype.map()` pour appliquer la fonction (`fn`) à chaque élément du premier tableau (`a`).
- Utilisez `Array.prototype.filter()` en combinaison avec la fonction (`fn`) sur le premier tableau (`a`) pour ne conserver que les valeurs qui ne sont pas contenues dans le second tableau (`b`), en utilisant `Set.prototype.has()`.

Voici le code de la fonction :

```js
const differenceBy = (a, b, fn) => {
  const s = new Set(b.map(fn));
  return a.map(fn).filter((el) => !s.has(el));
};
```

Voici quelques exemples d'utilisation de la fonction :

```js
differenceBy([2.1, 1.2], [2.3, 3.4], Math.floor); // [1]
differenceBy([{ x: 2 }, { x: 1 }], [{ x: 1 }], (v) => v.x); // [2]
```
