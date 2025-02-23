# Vérifiez si deux URL sont de la même origine

Pour vérifier si deux URL sont de la même origine :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.

2. Utilisez `URL.protocol` et `URL.host` pour vérifier si les deux URL ont le même protocole et le même hôte.

```js
const isSameOrigin = (origin, destination) =>
  origin.protocol === destination.protocol && origin.host === destination.host;
```

3. Créez deux objets URL avec les URL que vous souhaitez comparer.

```js
const origin = new URL("https://www.30secondsofcode.org/about");
const destination = new URL("https://www.30secondsofcode.org/contact");
```

4. Appelez la fonction `isSameOrigin` avec les deux objets URL en arguments pour obtenir une sortie booléenne.

```js
isSameOrigin(origin, destination); // true
```

5. Vous pouvez également tester la fonction avec d'autres URL pour voir si elles sont de la même origine ou non.

```js
const other = new URL("https://developer.mozilla.org");
isSameOrigin(origin, other); // false
```
