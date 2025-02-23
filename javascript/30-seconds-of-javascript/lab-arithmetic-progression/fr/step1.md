# Exemple de code de progression arithmétique

Pour pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.

Voici un exemple de code qui crée un tableau de nombres en progression arithmétique. Le tableau commence par un entier positif donné et va jusqu'à une limite spécifiée :

```js
const arithmeticProgression = (n, lim) =>
  Array.from({ length: Math.ceil(lim / n) }, (_, i) => (i + 1) * n);
```

Pour utiliser ce code, appelez simplement la fonction `arithmeticProgression` avec deux arguments : l'entier positif de départ et la limite. Par exemple :

```js
arithmeticProgression(5, 25); // [5, 10, 15, 20, 25]
```
